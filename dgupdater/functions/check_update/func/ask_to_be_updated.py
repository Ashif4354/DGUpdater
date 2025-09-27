from subprocess import run
from shutil import which

def ask_to_be_updated(this_os: str) -> bool:
    question: str = "New update is available for the application. Do you want to update now?"
    try:
        if this_os == 'Darwin':
            if which('osascript'):
                result = run(
                    [
                        'osascript',
                        '-e',
                        f"display dialog {question}"
                        + ' buttons {"Yes", "No"} default button "No"',
                    ],
                    capture_output=True,
                )

                return result.returncode == 0
            
            return False
        
        elif this_os == 'Linux':
            if which('zenity'):
                result = run(
                    [
                        'zenity', 
                        '--question', 
                        '--text', 
                        question
                    ], 
                    capture_output=True
                )

                return result.returncode == 0
            
            return False

        elif this_os == 'Windows':
            from ctypes import windll
            result = windll.user32.MessageBoxW(0, question, "Update", 4)

            return result == 6
        
        else:
            raise OSError(f'Unsupported OS: {this_os}')
    
    except Exception as _:
        return False
    

if __name__ == '__main__':
    print(ask_to_be_updated('Darwin'))