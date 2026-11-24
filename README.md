# Password Strength Checker

A lightweight, command-line Python tool that evaluates password strength against common security best practices and checks for known leaked passwords.

## Features
* **Common Password Detection:** Uses O(1) set lookups to instantly flag passwords found in the NCSC 100k most-used passwords list.
* **Comprehensive Scoring (0–6 Scale):** Evaluates passwords based on length (8+ and 12+ characters), uppercase letters, lowercase letters, numbers, and special characters.
* **Actionable Feedback:** Provides clear, specific suggestions on how to strengthen weak or moderate passwords.
* **Zero External Dependencies:** Built entirely with Python's standard library (`re` and `string`).

## Prerequisites
* **Python 3.x** installed on your system.
* The `100k-most-used-passwords-NCSC.txt` wordlist file placed in the same directory as the script (optional—the tool will still run with a warning if the file is missing).

## Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PsifiakiAsfaleia/password-strength-checker.git
   cd password-strength-checker
   ```

2. **Run the script:**
   ```bash
   python password_checker.py
   ```

3. **Test your passwords:**
   Enter any password when prompted to view its strength rating, score, and improvement tips. Type `exit` to close the program.

## Example Output

```text
Enter a password to test ( or type 'exit' to quit): hello123

Password Strength: Very Weak (Score: 0/6)
Suggestions to improve:
- Password was found in a common list. Avoid predictable words.
```

```text
Enter a password to test ( or type 'exit' to quit): Tr0ub4dor&3!

Password Strength: Very Strong (Score: 6/6)
```

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.

