
import os

score = 0

def user_exists(username):
    with open("/etc/passwd", "r") as f:
        users = [line.split(":")[0] for line in f]
    return username in users

def file_exists(filepath):
    return os.path.exists(filepath)

def main():
    global score
    if user_exists("ferb"):
        score += 20
    if user_exists("phineas"):
        score += 20
    if not user_exists("doofenshmirtz"):
        score += 20
    if not file_exists("/tmp/f"):
        score += 20
    if not file_exists("ssh_keylogger.py"):
        score += 20

    print(f"You scored {score} points out of 100")

if __name__ == "__main__":
    main()
