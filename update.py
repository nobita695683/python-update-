import os
import winsound
import psutil
import pymem
import requests
import time
import sys
import shutil
import threading
import customtkinter as ctk

# 🔹 Update link and file names
UPDATE_URL = "https://github.com/nobita695683/python-update-/raw/refs/heads/main/update.py"  # 👈 Replace with your GitHub link
LOCAL_SCRIPT = "main.py"
EXE_NAME = "main.exe"
TEMP_EXE_NAME = "main_main.exe"

# 🔹 Function to update the script
def update_script():
    status_label.configure(text="🔄 Updating script... Please wait.", text_color="orange")
    try:
        response = requests.get(UPDATE_URL)
        if response.status_code == 200:
            with open(LOCAL_SCRIPT, "w", encoding="utf-8") as file:
                file.write(response.text)
            status_label.configure(text="✅ Script updated successfully!", text_color="green")
            return True
        else:
            status_label.configure(text="❌ Failed to update script!", text_color="red")
            return False
    except Exception as e:
        status_label.configure(text=f"⚠️ Error: {e}", text_color="red")
        return False

# 🔹 Function to rebuild EXE
def rebuild_exe():
    status_label.configure(text="🔄 Rebuilding EXE... Please wait.", text_color="orange")
    try:
        os.system(f'pyinstaller --onefile --noconsole {LOCAL_SCRIPT}')
        if os.path.exists(f"dist/{EXE_NAME}"):
            shutil.move(f"dist/{EXE_NAME}", TEMP_EXE_NAME)
            status_label.configure(text="✅ EXE updated successfully!", text_color="green")
            return True
        else:
            status_label.configure(text="❌ Failed to create EXE!", text_color="red")
            return False
    except Exception as e:
        status_label.configure(text=f"⚠️ Error: {e}", text_color="red")
        return False

# 🔹 Function to restart EXE
def restart_exe():
    status_label.configure(text="🚀 Restarting application...", text_color="blue")
    time.sleep(2)
    os.replace(TEMP_EXE_NAME, EXE_NAME)  # Replace old EXE with new EXE
    os.system(EXE_NAME)
    sys.exit()

# 🔹 Run script update in a separate thread
def run_code_update():
    threading.Thread(target=update_script, daemon=True).start()

# 🔹 Run EXE update in a separate thread
def run_exe_update():
    def process():
        if rebuild_exe():
            restart_exe()
    
    threading.Thread(target=process, daemon=True).start()


def emote_100():
    search = rb"\x60\x40\xCD\xCC\x8C\x3F\x8F\xC2\xF5\x3C\xCD\xCC\xCC\x3D\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xF0\x41\x00\x00\x48\x42\x00\x00\x00\x3F\x33\x33\x13\x40\x00\x00\xB0\x3F\x00\x00\x80\x3F\x01"
    replace = b"\x60\x40\xCD\xCC\x8C\x3F\x8F\xC2\xF5\x3C\xCD\xCC\xCC\x3D\x06\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\xF0\x41\x00\x00\x48\x42\x00\x00\x00\x3F\x33\x33\x13\x40\x00\x00\xB0\x3F\x00\x00\x80\x3F\x01"

     # Check if HD-Player.exe is running
    hd_player_running = False
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'HD-Player.exe':
            hd_player_running = True
            break

    if not hd_player_running:
        status_label.configure(text="No Found HD-Player.exe", text_color="red")
        return

    # Memory Patch Apply
    status = scan_and_replace("HD-Player.exe", search, replace)

    if status:
        status_label.configure(text="100 Level Enabled!", text_color="green")
    else:
        status_label.configure(text="100 Level Failed!", text_color="red")

    # Play beep sound after scan process is complete
    winsound.Beep(1000, 500)  # Frequency = 1000 Hz, Duration = 500 ms



# 🔹 CustomTkinter UI Setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Software Updater")
root.geometry("400x300")

# 🏷️ Status Label
status_label = ctk.CTkLabel(root, text="👋 Welcome!", font=("Arial", 16))
status_label.pack(pady=20)

# 🟢 Update Script Button
code_update_button = ctk.CTkButton(root, text="📝 Update Script", command=run_code_update, fg_color="green")
code_update_button.pack(pady=10)

# 🔵 Update EXE Button
exe_update_button = ctk.CTkButton(root, text="⚙️ Update EXE", command=run_exe_update, fg_color="blue")
exe_update_button.pack(pady=10)

emulator_bypass_checkbox_var = ctk.BooleanVar()
emulator_bypass_checkbox = ctk.CTkCheckBox(root, text="100 Level", variable=emulator_bypass_checkbox_var, command=emote_100)
emulator_bypass_checkbox.place(relx=0.1, rely=0.7)  # ডান পাশে





def scan_and_replace(processName, search, replace):
    try:
        pm = pymem.Pymem(processName)
        matches = pm.pattern_scan_all(search, return_multiple=True)

        if not matches:
            return False
        
        if len(matches) == 1:
            print("One value found")
        else:
            print(f"Warning: multiple values found ({len(matches)})!")

        for match in matches:
            pm.write_bytes(match, replace, len(replace))

        return True

    except Exception as e:
        print(f"Error: {e}")
        return False










# ▶️ Run the UI
root.mainloop()
