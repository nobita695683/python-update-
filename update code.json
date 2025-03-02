import os
import winsound
import customtkinter as ctk
import keyboard
import pymem
import sys
from pymem import memory
import win32com.shell.shell as shell
import Memory

ASADMIN = 'asadmin'

if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    sys.exit(0)

# Initialize GUI
root = ctk.CTk()
root.geometry("400x300")
root.title("DLL Injector")

# Global Variables
pm = None
landing_addresses = []
landing_original_bytes = None

# Status Label
label_status = ctk.CTkLabel(root, text="Waiting for action...", text_color="blue")
label_status.pack(pady=10)

# Inject Button
landing_button = ctk.CTkButton(root, text="Activate Landing", fg_color="green", command=lambda: toggle_landing())
landing_button.place(relx=0.1, rely=0.2)

import threading

def toggle_landing():
    threading.Thread(target=_toggle_landing, daemon=True).start()

def _toggle_landing():
    global pm, landing_addresses, landing_original_bytes
    try:
        label_status.configure(text="Processing...", text_color="white")
        root.update_idletasks()

        if pm is None:
            pm = pymem.Pymem("HD-Player.exe")

        if not landing_addresses:
            address = Memory.find_pattern(pm, rb"\x00\x00\x00\x00\x00\x00\x80\x3f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xbf\x00\x00\x00\x00\x00\x00\x80\xbf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x3f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x3f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xbf\x00\x00\x80\x7f\x00\x00\x80\x7f\x00\x00\x80\x7f\x00\x00\x80\xff")
            if not address:
                label_status.configure(text="No matching address!", text_color="red")
                return
            landing_addresses.append(address)
            landing_original_bytes = pm.read_bytes(address, 40)

        is_activated = landing_button.cget("text") == "Activate Landing"
        replace = (b"\x00\x00\x00\x00\x00\x00\x00\x43") if is_activated else landing_original_bytes
        pm.write_bytes(landing_addresses[0], replace, len(replace))

        if is_activated:
            landing_button.configure(text="Deactivate Landing", fg_color="red")
            label_status.configure(text="Landing Activated", text_color="green")
            winsound.Beep(1000, 500)
        else:
            landing_button.configure(text="Activate Landing", fg_color="green")
            label_status.configure(text="Landing Deactivated", text_color="red")

    except Exception as e:
        label_status.configure(text=f"Error: {e}", text_color="red")

# Hotkey Setup
hotkey = "F5"
keyboard.add_hotkey(hotkey, toggle_landing, suppress=False, trigger_on_release=False, timeout=0)

# Start GUI
root.mainloop()
আমাকে সেক্স বক্স বাটন বানায় দাও জানিয়ে এভাবে হট কি কাজ করে
