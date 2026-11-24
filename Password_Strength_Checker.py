import re
import string

# Load common passwords once as a set for fast O(1) lookups
try:
    with open(
        '100k-most-used-passwords-NCSC.txt',
        'r',
        encoding='utf-8',
        errors='ignore',
    ) as f:
        COMMON_PASSWORDS = set(line.strip().lower() for line in f)
except FileNotFoundError:
    print(
        'Warning: Common password file not found. Skipping common password'
        ' check.'
    )
    COMMON_PASSWORDS = set()


def check_password_strength(password):
    """Function to check the strength of a password."""
    score = 0
    feedback = []

    # 1. Common Password Check
    if password.lower() in COMMON_PASSWORDS:
        feedback.append(
            'Password was found in a common list. Avoid predictable words.'
        )
        return 'Very Weak', 0, feedback

    # 2. Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append('Use at least 8 characters (12+ is best).')

    # 3. Uppercase Check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append('Add at least one uppercase letter.')

    # 4. Lowercase Check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append('Add at least one lowercase letter.')

    # 5. Number Check
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append('Include at least one number.')

    # 6. Special Character Check
    if re.search(f'[{re.escape(string.punctuation)}]', password):
        score += 1
    else:
        feedback.append('Include at least one special character (!@#$%&*).')

    # Determine Final Score
    if score >= 6:
        strength = 'Very Strong'
    elif score >= 4:
        strength = 'Moderate'
    else:
        strength = 'Weak'

    return strength, score, feedback


def password_checker():
    ToolName = r"""
 ____                                     _ 
|  _ \ __ _ ___ _____      _____  _ __ __| |
| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |
|  __/ (_| \__ \__ \\ V  V / (_) | | | (_| |
|_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|
                                            
 ____  _                        _   _     
/ ___|| |_ _ __ ___ _ __   __ _| |_| |__  
\___ \| __| '__/ _ \ '_ \ / _` | __| '_ \ 
 ___) | |_| | |  __/ | | | (_| | |_| | | |
|____/ \__|_|  \___|_| |_|\__, |\__|_| |_|
                          |___/           
  ____ _               _             
 / ___| |__   ___  ___| | _____ _ __ 
| |   | '_ \ / _ \/ __| |/ / _ \ '__|
| |___| | | |  __/ (__|   <  __/ |   
 \____|_| |_|\___|\___|_|\_\___|_|   

"""
    print(ToolName)

    while True:
        user_pw = input("\nEnter a password to test ( or type 'exit' to quit): ")

        if user_pw.lower() == 'exit':
            print('Thank you for using this tool.')
            break

        strength, score, tips = check_password_strength(user_pw)

        print(f'\nPassword Strength: {strength} (Score: {score}/6)')
        if tips:
            print('Suggestions to improve:')
            for tip in tips:
                print(f'- {tip}')


if __name__ == '__main__':
    password_checker()

