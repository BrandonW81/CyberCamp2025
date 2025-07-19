import os

score = 0

def user_exists(username):
    with open("/etc/passwd", "r") as f:
        users = [line.split(":")[0] for line in f]
    return username in users

def file_exists_anywhere(filename):
    try:
        for root, dirs, files in os.walk("/"):
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            for file in files:
                if file == filename:
                    return True
    except Exception:
        pass
    return False

def program_with_name_exists(partial_name):
    partial_name = partial_name.lower()
    for root, dirs, files in os.walk("/"):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        try:
            for file in files:
                if partial_name in file.lower():
                    return True
        except PermissionError:
            continue
        except Exception:
            continue
    return False

def main():
    global score

    if user_exists("owcaintern"):
        score += 5
    if user_exists("perry"):
        score += 5
    if user_exists("carl"):
        score += 5
    if user_exists("peter"):
        score += 5
    if user_exists("pinky"):
        score += 5
    if user_exists("terry"):
        score += 5
    if user_exists("planty"):
        score += 5
    if user_exists("harry"):
        score += 5

    if not user_exists("doof"):
        score += 20
    if not user_exists("evil-intern"):
        score += 20

    if not file_exists_anywhere("ssh_keylogger.py"):
        score += 10
    if not file_exists_anywhere("lebron.png"):
        score += 10

    # Now check if Firefox is present — add points if yes
    if program_with_name_exists("firefox"):
        score += 10

    # Check if Thunderbird is present — add points if yes
    if program_with_name_exists("thunderbird"):
        score += 10

    print(f"You scored {score} points.")

if __name__ == "__main__":
    main()
