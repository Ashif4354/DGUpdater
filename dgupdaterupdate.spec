# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path
from platform import system

ROOT: str = Path(".").resolve()

match system():
    case "Windows":
        this_os = "win"
    case "Darwin":
        this_os = "mac"
    case "Linux":
        this_os = "lin"
    case _:
        raise OSError(f"Unsupported OS: {system()}")

a = Analysis(
    [str(ROOT / "dgupdaterupdate.py")],
    pathex=[str(ROOT)],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name=f'dgupdaterupdate_{this_os}',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=[str(ROOT / "assets" / "loading-arrow.ico")],
)
