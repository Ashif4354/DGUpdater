#!/usr/bin/env python3
"""
Cross-platform build script for DGUpdater executable.
Replaces the Windows-only build-update-exe.bat file.
"""

import platform
import subprocess
import sys
import os
from pathlib import Path

def build_executable():
    """Build the update executable for the current platform."""
    
    if platform.system() == "Windows":
        # On Windows, try to build exe using auto-py-to-exe or pyinstaller
        try:
            # Try auto-py-to-exe first (if available)
            output_dir = Path("dgupdater/bin")
            result = subprocess.run([
                "auto-py-to-exe", 
                "-c", "apte-update-conf.json", 
                "-o", str(output_dir)
            ], check=True)
            print("✅ Windows executable built successfully using auto-py-to-exe")
            
        except (subprocess.CalledProcessError, FileNotFoundError):
            # Fallback to pyinstaller
            try:
                output_dir = Path("dgupdater/bin")
                output_dir.mkdir(parents=True, exist_ok=True)
                
                result = subprocess.run([
                    "pyinstaller",
                    "--onefile",
                    "--console", 
                    "--name", "dgupdaterupdate",
                    "--distpath", str(output_dir),
                    "update.py"
                ], check=True)
                print("✅ Windows executable built successfully using PyInstaller")
                
            except (subprocess.CalledProcessError, FileNotFoundError):
                print("❌ Error: Neither auto-py-to-exe nor pyinstaller is available.")
                print("Please install one of them:")
                print("  pip install auto-py-to-exe")
                print("  pip install pyinstaller")
                sys.exit(1)
    else:
        # On Unix-like systems, just ensure the Python script is available
        print(f"ℹ️  On {platform.system()}, using Python script directly (no compilation needed)")
        print("✅ Cross-platform support ready")

if __name__ == "__main__":
    print(f"🔨 Building DGUpdater for {platform.system()}...")
    build_executable()
    print("🎉 Build process completed!")