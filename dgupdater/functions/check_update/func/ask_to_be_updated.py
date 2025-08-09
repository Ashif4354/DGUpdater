import platform
import sys


def _show_windows_messagebox(title: str, message: str) -> bool:
    """Show message box on Windows using ctypes."""
    try:
        import ctypes
        # MB_YESNO = 4, IDYES = 6
        result = ctypes.windll.user32.MessageBoxW(0, message, title, 4)
        return result == 6  # IDYES
    except Exception:
        return _show_console_prompt(title, message)


def _show_linux_messagebox(title: str, message: str) -> bool:
    """Show message box on Linux using available GUI tools or console fallback."""
    # Try zenity first (common on GNOME systems)
    try:
        import subprocess
        result = subprocess.run(
            ['zenity', '--question', '--text', message, '--title', title],
            capture_output=True
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.SubprocessError):
        pass
    
    # Try kdialog (common on KDE systems)
    try:
        import subprocess
        result = subprocess.run(
            ['kdialog', '--yesno', message, '--title', title],
            capture_output=True
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.SubprocessError):
        pass
    
    # Fallback to console
    return _show_console_prompt(title, message)


def _show_macos_messagebox(title: str, message: str) -> bool:
    """Show message box on macOS using osascript."""
    try:
        import subprocess
        script = f'''display dialog "{message}" with title "{title}" buttons {{"No", "Yes"}} default button "Yes"'''
        result = subprocess.run(
            ['osascript', '-e', script],
            capture_output=True
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.SubprocessError):
        return _show_console_prompt(title, message)


def _show_console_prompt(title: str, message: str) -> bool:
    """Show console prompt - universal fallback."""
    print(f"\n{title}")
    print("=" * len(title))
    print(f"{message}")
    
    while True:
        response = input("Do you want to update now? (y/n): ").strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'.")


def ask_to_be_updated() -> bool:
    """Ask user if they want to update the application using platform-appropriate method."""
    title = "Update"
    message = "New update is available for the application. Do you want to update now?"
    
    system = platform.system().lower()
    
    if system == 'windows':
        return _show_windows_messagebox(title, message)
    elif system == 'linux':
        return _show_linux_messagebox(title, message)
    elif system == 'darwin':  # macOS
        return _show_macos_messagebox(title, message)
    else:
        # Unknown platform, use console fallback
        return _show_console_prompt(title, message)  
