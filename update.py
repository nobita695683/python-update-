import os
import requests
import time
import sys
import shutil
import threading
import tkinter as tk
import psutil
import pymem

# 🔹 আপডেট লিঙ্ক এবং ফাইলের নাম
UPDATE_URL = "https://github.com/nobita695683/python-update-/raw/refs/heads/main/update.py"  # 👈 এখানে আপনার GitHub লিঙ্ক দিন
LOCAL_SCRIPT = "main.py"
EXE_NAME = "main.exe"
TEMP_EXE_NAME = "main_main.exe"

def update_script():
    """গিটহাব থেকে নতুন কোড ডাউনলোড করে আপডেট করে"""
    label.config(text="🔄 কোড আপডেট হচ্ছে... দয়া করে অপেক্ষা করুন।")
    try:
        response = requests.get(UPDATE_URL)
        if response.status_code == 200:
            with open(LOCAL_SCRIPT, "w", encoding="utf-8") as file:
                file.write(response.text)
            label.config(text="✅ কোড আপডেট সফল হয়েছে!")
            return True
        else:
            label.config(text="❌ কোড আপডেট ব্যর্থ হয়েছে!")
            return False
    except Exception as e:
        label.config(text=f"⚠️ ত্রুটি: {e}")
        return False

def rebuild_exe():
    """PyInstaller ব্যবহার করে EXE ফাইল পুনরায় তৈরি করে"""
    label.config(text="🔄 EXE পুনরায় তৈরি হচ্ছে... দয়া করে অপেক্ষা করুন।")
    try:
        os.system(f'pyinstaller --onefile --noconsole {LOCAL_SCRIPT}')
        if os.path.exists(f"dist/{EXE_NAME}"):
            shutil.move(f"dist/{EXE_NAME}", TEMP_EXE_NAME)
            label.config(text="✅ EXE সফলভাবে আপডেট হয়েছে!")
            return True
        else:
            label.config(text="❌ EXE তৈরি ব্যর্থ হয়েছে!")
            return False
    except Exception as e:
        label.config(text=f"⚠️ ত্রুটি: {e}")
        return False

def restart_exe():
    """নতুন EXE ফাইল চালু করে এবং পুরানোটি বন্ধ করে"""
    label.config(text="🚀 সফটওয়্যার পুনরায় চালু হচ্ছে...")
    time.sleep(2)
    os.replace(TEMP_EXE_NAME, EXE_NAME)  # পুরানো EXE পরিবর্তন করে নতুন EXE রাখে
    os.system(EXE_NAME)
    sys.exit()

def run_code_update():
    """শুধুমাত্র কোড আপডেট করবে (EXE তৈরি করবে না)"""
    threading.Thread(target=update_script, daemon=True).start()

def run_exe_update():
    """শুধুমাত্র EXE আপডেট করবে (কোড আপডেট করবে না)"""
    def process():
        if rebuild_exe():
            restart_exe()
    
    threading.Thread(target=process, daemon=True).start()

# 🔹 Tkinter UI তৈরি করুন
root = tk.Tk()
root.title("সফটওয়্যার আপডেটার")
root.geometry("400x300")

label_status = ctk.CTkLabel(root, text="☢", text_color="white")
label_status.pack(side="bottom", anchor="sw", padx=10, pady=0.5)
# 🏷️ লেবেল উইজেট
label = tk.Label(root, text="👋 স্বাগতম!", font=("Arial", 14))
label.pack(pady=20)

# 🟢 কোড আপডেট বাটন (শুধুমাত্র কোড আপডেট করবে)
code_update_button = tk.Button(root, text="📝 কোড আপডেট করুন", command=run_code_update)
code_update_button.pack(pady=10)

# 🔵 EXE আপডেট বাটন (শুধুমাত্র EXE আপডেট ও রিস্টার্ট করবে)
exe_update_button = tk.Button(root, text="⚙️ EXE আপডেট করুন", command=run_exe_update)
exe_update_button.pack(pady=10)

emulator_bypass_checkbox_var = ctk.BooleanVar()
emulator_bypass_checkbox = ctk.CTkCheckBox(root, text="100 Level", variable=emulator_bypass_checkbox_var, command=emote_100)
emulator_bypass_checkbox.place(relx=0.1, rely=0.4)  # ডান পাশে
def emote_100():
    search = rb"\x41\x3D\x2E\x36"
    replace = b"\x57\xE1\x2E\x36"

     # Check if HD-Player.exe is running
    hd_player_running = False
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'HD-Player.exe':
            hd_player_running = True
            break

    if not hd_player_running:
        label_status.configure(text="No Found HD-Player.exe", text_color="red")
        return

    # Memory Patch Apply
    status = Memory.scan_and_replace("HD-Player.exe", search, replace)

    if status:
        label_status.configure(text="100 Level Enabled!", text_color="green")
    else:
        label_status.configure(text="100 Level Failed!", text_color="red")

    # Play beep sound after scan process is complete




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

def get_process(procesName):
    try:
        pm = pymem.Pymem(procesName)
        print('Process Found Please Continue')
        return pm.process_id
    except:
        print('Process Not Found Waiting for process')
        return False





























# ▶️ Tkinter মেইন লুপ চালু করুন
root.mainloop()
