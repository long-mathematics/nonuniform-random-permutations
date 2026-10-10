#!/usr/bin/env python3
"""Replay finite audits and rebuild the standalone manuscript deterministically.

No remote service is changed. Frozen provenance and expected results are read-only.
The optional --skip-build flag runs finite checks without a TeX installation.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
PROV = ROOT / 'notes/provenance/thorp-cycle-universality'
SOURCE = ROOT / 'papers/08-thorp-cycle-universality/thorp-cycle-universality.tex'
SNAPSHOT = ROOT / 'output/pdf/thorp-cycle-universality.pdf'
WORK = ROOT / '.build/thorp-cycle-universality-checks'

def digest(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def command(args: list[str], *, cwd: Path, env: dict[str,str] | None = None) -> subprocess.CompletedProcess[str]:
    p = subprocess.run(args, cwd=cwd, env=env, capture_output=True, text=True, timeout=300)
    if p.returncode:
        raise RuntimeError(f"Command failed: {' '.join(args)}\n{p.stdout[-4000:]}\n{p.stderr[-4000:]}")
    return p

def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skip-build', action='store_true')
    args=parser.parse_args()
    WORK.mkdir(parents=True, exist_ok=True)
    report: dict = {'finite_checks': [], 'build': 'not requested'}
    with tempfile.TemporaryDirectory(prefix='core-',dir=WORK) as tmpname:
        dest=Path(tmpname)
        with zipfile.ZipFile(PROV/'reviewed-v1-archive.zip') as archive:
            for name in archive.namelist():
                if not (dest/name).resolve().is_relative_to(dest.resolve()):
                    raise RuntimeError('Unsafe path in the historical archive')
            archive.extractall(dest)
        drivers=list(dest.glob('*/reproduce.py'))
        if len(drivers)!=1:
            raise RuntimeError('Expected one historical reproduction driver')
        p=command([sys.executable,str(drivers[0])],cwd=dest)
        core=json.loads(p.stdout)
        if core['status']!='all reruns match preserved results':
            raise AssertionError('Historical result changed')
        (WORK/'core_reproduction.json').write_text(json.dumps(core,indent=2)+'\n')
        report['finite_checks'].append({'name':'preserved_core_suite','status':'passed','checks':core['checks']})
    p=command([sys.executable,str(HERE/'audit_additions.py')],cwd=WORK)
    actual=json.loads(p.stdout)
    expected=json.loads((PROV/'validation/addition_audit_results.json').read_text())
    if actual!=expected:
        raise AssertionError('The additions audit differs from the frozen expected output')
    (WORK/'addition_audit_results.json').write_text(json.dumps(actual,indent=2)+'\n')
    report['finite_checks'].append({'name':'additions_suite','status':'matches frozen results'})
    source=SOURCE.read_text()
    labels=re.findall(r'\\label\{([^}]+)\}',source)
    refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',source)
    if len(set(labels))!=len(labels) or set(refs)-set(labels):
        raise AssertionError('Duplicate or missing source label')
    if not args.skip_build:
        for name in ('latexmk','pdflatex'):
            if shutil.which(name) is None:
                raise RuntimeError(f'Missing {name}; use --skip-build for finite checks only')
        env=dict(os.environ,SOURCE_DATE_EPOCH='1791504000',FORCE_SOURCE_DATE='1',TZ='UTC')
        hashes=[]
        for i in (1,2):
            out=WORK/f'clean-build-{i}'
            if out.exists():shutil.rmtree(out)
            out.mkdir()
            cmd=['latexmk','-pdf','-g','-interaction=nonstopmode','-halt-on-error',
                 '-file-line-error','-latexoption=-no-shell-escape','-outdir='+str(out),SOURCE.name]
            p=command(cmd,cwd=SOURCE.parent,env=env)
            (out/'console.txt').write_text(p.stdout+p.stderr)
            log=(out/(SOURCE.stem+'.log')).read_text(errors='replace')
            bad=[line for line in log.splitlines() if re.search(r'^!|Overfull|undefined|multiply defined',line)]
            if bad:raise RuntimeError('LaTeX diagnostics:\n'+'\n'.join(bad))
            hashes.append(digest(out/(SOURCE.stem+'.pdf')))
        if hashes[0]!=hashes[1] or hashes[0]!=digest(SNAPSHOT):
            raise AssertionError('Rebuilt PDF differs from the frozen snapshot; check TeX toolchain versions')
        report['build']={'status':'two clean builds match snapshot','pdf_sha256':hashes[0],
                         'source_sha256':digest(SOURCE)}
    report['status']='all requested checks passed'
    (WORK/'summary.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    try:
        main()
    except (AssertionError, RuntimeError, OSError, subprocess.SubprocessError, ValueError) as exc:
        print(str(exc),file=sys.stderr)
        sys.exit(1)
