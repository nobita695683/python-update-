import requests
import winsound
import customtkinter as ctk
import keyboard
import pymem

# Initialize global variables
pm = None  
camera_addresses = []
camera_original_bytes = None 

def find_pattern(pm, pattern):
    matches = pm.pattern_scan_all(pattern, return_multiple=True)
    return matches[0] if matches and len(matches) == 1 else None

def toggle_camera():
    global pm, camera_addresses, camera_original_bytes
    try:
        label_status.configure(text="Processing...", text_color="white")
        root.update_idletasks()

        if pm is None:
            pm = pymem.Pymem("HD-Player.exe")

        if not camera_addresses:
            address = find_pattern(pm, rb"\x00\x00\x00\x00\x00\x00\x80\x3f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xbf\x00\x00\x00\x00\x00\x00\x80\xbf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x3f\x00\x00")
            if not address:
                label_status.configure(text="No matching address!", text_color="red")
                return
            camera_addresses.append(address)
            camera_original_bytes = pm.read_bytes(address, 40)
        

        replace = b"\x00\x00\x00\x00\x00\x00\x80\x40" if camera_checkbox_var.get() else camera_original_bytes

        pm.write_bytes(camera_addresses[0], replace, len(replace))
        label_status.configure(
            text="Camera Activated" if camera_checkbox_var.get() else "Camera Deactivated",
            text_color="green" if camera_checkbox_var.get() else "red"
        )

        if camera_checkbox_var.get():
            winsound.Beep(1000, 500)

    except Exception as e:
        label_status.configure(text=f"Error: {e}", text_color="red")


def toggle_landing():
    global pm, camera_addresses, camera_original_bytes
    try:
        label_status.configure(text="Processing...", text_color="white")
        root.update_idletasks()

        if pm is None:
            pm = pymem.Pymem("HD-Player.exe")

        if not camera_addresses:
            label_status.configure(text="No camera address found!", text_color="red")
            return

        replace = b"\x00\x00\x00\x00\x00\x00\x80\x43" if landing_checkbox_var.get() else camera_original_bytes

        pm.write_bytes(camera_addresses[0], replace, len(replace))
        label_status.configure(
            text="Landing Activated" if landing_checkbox_var.get() else "Landing Deactivated",
            text_color="green" if landing_checkbox_var.get() else "red"
        )

        if landing_checkbox_var.get():
            winsound.Beep(1000, 500)

    except Exception as e:
        label_status.configure(text=f"Error: {e}", text_color="red")


# ✅ GUI Setup
root = ctk.CTk()
root.title("Sniper Scope Modifier")
root.geometry("400x300")

camera_checkbox_var = ctk.BooleanVar()
camera_checkbox = ctk.CTkCheckBox(root, text="Camera", variable=camera_checkbox_var, command=toggle_camera)
camera_checkbox.place(relx=0.1, rely=0.4)

landing_checkbox_var = ctk.BooleanVar()
landing_checkbox = ctk.CTkCheckBox(root, text="Landing", variable=landing_checkbox_var, command=toggle_landing)
landing_checkbox.place(relx=0.1, rely=0.5)  

label_status = ctk.CTkLabel(root, text="🔍 Status: Waiting...", text_color="black")
label_status.pack(pady=10)
# Function to handle hotkey and toggle sniper scope
def handle_hotkey():
    # Toggle the checkbox state when 'Ctrl + 1' is pressed
    camera_checkbox_var.set(not camera_checkbox_var.get())  # Toggle the checkbox value
    toggle_camera()  # Call the function to update the scope status

# Add the hotkey for 'Ctrl + 1'
keyboard.add_hotkey('ctrl+1', handle_hotkey) 

























# 🔹 GitHub link to check for updates (Raw URL)
UPDATE_URL = "https://github.com/nobita695683/python-update-/raw/refs/heads/main/update.py"  # 👈 Provide your GitHub link
LOCAL_SCRIPT = "main.py"  # 👈 Local script name

def update_script():
    """Only updates the modified lines, does not add or delete new lines"""
    try:
        response = requests.get(UPDATE_URL)
        if response.status_code == 200:
            new_lines = response.text.splitlines()  # Fetches the new code line by line
            with open(LOCAL_SCRIPT, "r", encoding="utf-8") as file:
                old_lines = file.read().splitlines()

            updated_lines = old_lines.copy()  # Keeps the old code and updates only modified lines
            changes_made = False

            # Compare new and old lines, updating only modified lines
            min_lines = min(len(old_lines), len(new_lines))
            for i in range(min_lines):
                if old_lines[i] != new_lines[i]:  # Only updated lines will be changed
                    updated_lines[i] = new_lines[i]
                    changes_made = True

            # If the new code has more lines than the old code
            if len(new_lines) > len(old_lines):
                updated_lines.extend(new_lines[len(old_lines):])

            if changes_made:
                with open(LOCAL_SCRIPT, "w", encoding="utf-8") as file:
                    file.write("\n".join(updated_lines) + "\n")
                print("✅ Only the modified lines have been updated!")
            else:
                print("✅ No changes found, no update required.")
        else:
            print("❌ Failed to fetch update from the server!")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

# 🔥 The script will automatically check for updates when executed
if __name__ == "__main__":
    update_script()
    print("🚀 The code has started!")

# Run the main event loop
root.mainloop()














































































