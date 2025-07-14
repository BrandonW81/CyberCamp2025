#!/usr/bin/env python3

password = "CarlTheIntern"  # The password the student must enter to defuse the bomb

print("🔥 WrongPasswordinator™ ACTIVATED! 🔥")
print("💥 If you fail to enter the correct password, the bomb will explode...")
print("🔐 You have one chance to stop it...\n")

user_input = input("Password: ")

if user_input == password:
    print("✅ BOMB DEFUSED! Password is correct.")
else:
    print("💥 BOOM! Wrong password. The tri-state area is in danger!\n")
    
    # Write failure log to a file
    with open("failed_attempt.txt", "w") as f:
        f.write("🚨 Failed password attempt detected.\n")
        f.write("Status: SYSTEM COMPROMISED.\n")

    # Print fake explosion
    print("🔥💣🔥💣🔥💣🔥💣🔥💣🔥💣🔥💣🔥💣🔥💣🔥💣🔥")
    print("""
              _.-^^---....,,--
          _--                  --_
         <                        >
         |                         |
          \._                   _./
             ```--. . , ; .--'''
                   | |   |
                .-=||  | |=-.
                `-=#$%&%$#=-'
                   | ;  :|
          _____.,-#%&$@%#&#~,._____
    """)
    print("☠️  SYSTEM FAILURE: THE TRI-STATE AREA IS NOW AT RISK ☠️")
