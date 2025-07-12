#!/usr/bin/env python3
import time

password = "platypus23"

while True:
    user_input = input("Enter password to start system boot: ")
    if user_input == password:
        print("Password correct! System is booting up...")
        print("Loading: ", end="", flush=True)
        for bran in range(20):
            print("#", end="", flush=True)
            time.sleep(0.2)
        print("\n✅ Systems are fully up!")
        break
    else:
        print("Incorrect password. Please try again.\n")
