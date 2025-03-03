import requests
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














































































