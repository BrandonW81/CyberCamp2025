import os
import subprocess

LOG_FILE = "system_check_log.txt"
score = 0

def log(message):
    with open(LOG_FILE, "w") as f:
        f.write(message + "\n")

def user_exists(username, users):
    return username in users

def banned_user_absent(username, users):
    return username not in users

def check_users():
    global score
    with open("/etc/passwd", "r") as f:
        users = [line.split(":")[0] for line in f]

    points = 0
    log_messages = []

    # Check ferb
    if user_exists("ferb", users):
        print("[✔] User 'ferb' exists.")
        points += 20
        log_messages.append("✅ 20 pts: User 'ferb' found.")
    else:
        print("[✘] User 'ferb' NOT found.")
        log_messages.append("❌ 0 pts: User 'ferb' missing.")

    # Check phineas
    if user_exists("phineas", users):
        print("[✔] User 'phineas' exists.")
        points += 20
        log_messages.append("✅ 20 pts: User 'phineas' found.")
    else:
        print("[✘] User 'phineas' NOT found.")
        log_messages.append("❌ 0 pts: User 'phineas' missing.")

    # Check doofenshmirtz banned user absent
    if banned_user_absent("doofenshmirtz", users):
        print("[✔] Banned user 'doofenshmirtz' NOT found.")
        points += 20
        log_messages.append("✅ 20 pts: Banned user 'doofenshmirtz' absent.")
    else:
        print("[✘] Banned user 'doofenshmirtz' FOUND.")
        log_messages.append("❌ 0 pts: Banned user 'doofenshmirtz' present.")

    score += points
    return points, log_messages

def check_backdoor():
    global score
    points = 0
    log_messages = []

    BACKDOOR_FIFO = "/tmp/f"
    SUSPICIOUS_FILE = "ssh_keylogger.py"

    # Check named pipe
    if not os.path.exists(BACKDOOR_FIFO):
        print(f"[✔] No suspicious named pipe at {BACKDOOR_FIFO}")
        points += 20
        log_messages.append(f"✅ 20 pts: No named pipe {BACKDOOR_FIFO}.")
    else:
        print(f"[✘] Suspicious named pipe found at {BACKDOOR_FIFO}")
        log_messages.append(f"❌ 0 pts: Named pipe {BACKDOOR_FIFO} found.")

    # Check suspicious file
    if not os.path.exists(SUSPICIOUS_FILE):
        print(f"[✔] Suspicious file '{SUSPICIOUS_FILE}' not found.")
        points += 20
        log_messages.append(f"✅ 20 pts: Suspicious file '{SUSPICIOUS_FILE}' absent.")
    else:
        print(f"[✘] Suspicious file '{SUSPICIOUS_FILE}' found!")
        log_messages.append(f"❌ 0 pts: Suspicious file '{SUSPICIOUS_FILE}' present.")

    score += points
    return points, log_messages

if __name__ == "__main__":
    print("=== SYSTEM INTEGRITY CHECK ===\n")

    user_points, user_logs = check_users()
    backdoor_points, backdoor_logs = check_backdoor()

    print(f"\nUser Check Score: {user_points} / 60")
    print(f"Backdoor Check Score: {backdoor_points} / 40")
    total_score = user_points + backdoor_points
    print(f"\nFINAL SCORE: {total_score} / 100")

    # Write logs
    with open(LOG_FILE, "w") as f:
        for line in user_logs + backdoor_logs:
            f.write(line + "\n")
        f.write(f"\nTotal Score: {total_score} / 100\n")
