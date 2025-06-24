from tkinter import messagebox

def ask_to_be_updated() -> bool:
    return messagebox.askyesno("Update", "New update is available for the application. Do you want to update now?")  
