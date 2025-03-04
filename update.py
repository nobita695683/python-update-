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

# 🔹 GitHub raw link to fetch updates
UPDATE_URL = "https://github.com/nobita695683/python-update-/raw/refs/heads/main/update.py"  # 👈 তোমার GitHub লিঙ্ক
LOCAL_SCRIPT = "main.py"  # স্ক্রিপ্ট ফাইলের নাম
EXE_NAME = "main.exe"  # এক্সিকিউটেবল ফাইলের নাম

# CustomTkinter উইন্ডো সেটআপ
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Home Page")
root.geometry("400x300")

# লেবেল উইজেট
label = ctk.CTkLabel(root, text="Welcome!", font=("Arial", 18))
label.pack(pady=20)

status_label = ctk.CTkLabel(root, text="Status: Ready", font=("Arial", 12))
status_label.pack(pady=10)





def update_script():
    """GitHub থেকে আপডেট স্ক্রিপ্ট ডাউনলোড করে"""
    try:
        status_label.configure(text="Status: Downloading update...")
        response = requests.get(UPDATE_URL)
        if response.status_code == 200:
            new_code = response.text
            with open(LOCAL_SCRIPT, "w", encoding="utf-8") as file:
                file.write(new_code)
            status_label.configure(text="Status: Script updated successfully!")
            return True
        else:
            status_label.configure(text="Status: Failed to fetch update!")
            return False
    except Exception as e:
        status_label.configure(text=f"Status: Error - {e}")
        return False

def rebuild_exe():
    """PyInstaller দিয়ে EXE ফাইল পুনরায় বানায়"""
    try:
        status_label.configure(text="Status: Rebuilding EXE...")
        os.system(f'pyinstaller --onefile --noconsole {LOCAL_SCRIPT}')
        
        # নতুন EXE ফাইল মুভ করা
        if os.path.exists(f"dist/{EXE_NAME}"):
            shutil.move(f"dist/{EXE_NAME}", EXE_NAME)
            status_label.configure(text="Status: EXE updated successfully!")
            return True
        else:
            status_label.configure(text="Status: Failed to create EXE!")
            return False
    except Exception as e:
        status_label.configure(text=f"Status: Error - {e}")
        return False

def restart_exe():
    """নতুন EXE রিস্টার্ট করে"""
    status_label.configure(text="Status: Restarting application...")
    time.sleep(2)
    os.system(EXE_NAME)
    sys.exit()

def update_process():
    """ব্যাকগ্রাউন্ডে আপডেট প্রসেস চালায়"""
    if update_script():
        if rebuild_exe():
            restart_exe()

def start_update():
    """থ্রেড চালিয়ে GUI ব্লক না করে আপডেট শুরু করে"""
    threading.Thread(target=update_process, daemon=True).start()


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





emulator_bypass_checkbox_var = ctk.BooleanVar()
emulator_bypass_checkbox = ctk.CTkCheckBox(root, text="100 Level", variable=emulator_bypass_checkbox_var, command=emote_100)
emulator_bypass_checkbox.place(relx=0.1, rely=0.7)  # ডান পাশে





# আপডেট বাটন
update_button = ctk.CTkButton(root, text="Update", command=start_update)
update_button.pack(pady=20)

# GUI রান করানো
root.mainloop()
