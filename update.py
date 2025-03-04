import os
import requests
import time
import sys
import shutil
import tkinter as tk

def show_message():
    label.config(text="Welcome to the Home Page!")

# Create the main window
root = tk.Tk()
root.title("Home Page")
root.geometry("400x300")

# Create a label widget
label = tk.Label(root, text="Welcome!", font=("Arial", 14))
label.pack(pady=20)

# Create a button widget
button = tk.Button(root, text="Click me", command=show_message)
button.pack(pady=20)



# 🔹 GitHub raw link to fetch updates
UPDATE_URL = "https://raw.githubusercontent.com/yourusername/repository/main/main.py"  # 👈 Change this to your GitHub link
LOCAL_SCRIPT = "main.py"  # Your script name
EXE_NAME = "myapp.exe"  # Your EXE file name

def update_script():
    """Downloads updated script from GitHub and replaces old script"""
    try:
        response = requests.get(UPDATE_URL)
        if response.status_code == 200:
            new_code = response.text
            with open(LOCAL_SCRIPT, "w", encoding="utf-8") as file:
                file.write(new_code)
            print("✅ Script updated successfully!")
            return True
        else:
            print("❌ Failed to fetch update from the server!")
            return False
    except Exception as e:
        print(f"⚠️ Error occurred while updating: {e}")
        return False

def rebuild_exe():
    """Rebuilds the EXE using PyInstaller"""
    try:
        print("🔄 Rebuilding EXE...")
        os.system(f'pyinstaller --onefile --noconsole {LOCAL_SCRIPT}')
        
        # Move the new EXE to replace the old one
        if os.path.exists(f"dist/{EXE_NAME}"):
            shutil.move(f"dist/{EXE_NAME}", EXE_NAME)
            print("✅ EXE successfully updated!")
            return True
        else:
            print("❌ Failed to create new EXE!")
            return False
    except Exception as e:
        print(f"⚠️ Error occurred while rebuilding EXE: {e}")
        return False

def restart_exe():
    """Restarts the updated EXE"""
    print("🚀 Restarting application...")
    time.sleep(2)
    os.system(EXE_NAME)
    sys.exit()

if __name__ == "__main__":
    if update_script():
        if rebuild_exe():
            restart_exe()
# Run the main event loop
root.mainloop()
