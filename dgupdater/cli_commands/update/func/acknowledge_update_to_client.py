from tkinter import messagebox  

def acknowledge_update_to_client() -> None:
    messagebox.showinfo("Success", "Updated to the latest version. Please restart the application.")

if __name__ == "__main__":
    acknowledge_update_to_client()