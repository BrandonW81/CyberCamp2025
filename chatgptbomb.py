import os
import getpass
import time

password = "CarlTheIntern"

print("🔥 WrongPasswordinator™ ACTIVATED! 🔥")
print("💥 If you fail to enter the correct password, the bomb will explode...")
print("🔐 ...and your system password will be changed!")

user_input = input("Password: ")

if user_input == password:
    print("✅ BOMB DEFUSED! Password is correct.")
else:
    print("💥 BOOM! Wrong password. The tri-state area is doomed!")

    # Get the correct user even when running with sudo
    username = os.environ.get("SUDO_USER", getpass.getuser())

    print(f"[INFO] Changing password for user: {username}")
    os.system(f"echo '{username}:hanos900' | chpasswd")
    print("[INFO] Password change command executed.")

    print("[INFO] Rebooting system in 5 seconds...")
    time.sleep(5)
    os.system("reboot")
