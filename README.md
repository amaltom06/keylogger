# keylogger
**Description**

This project is a keylogger that captures and logs all keystrokes made by the user. The keylogger is implemented in Python using the pynput library, which provides a simple and efficient way to monitor and log keyboard events. It records every keystroke made by the user and saves this information to a log file. This can be useful for various educational purposes, such as understanding how keyloggers work, developing user activity monitoring tools, or conducting security research.

Important Note: This keylogger is intended for educational purposes only and should not be used for any malicious activities. Unauthorized use of keyloggers to capture and log keystrokes without the user's consent is illegal and unethical. Always ensure you have explicit permission to use this tool.

**Features**

Captures all keystrokes:
The keylogger captures every keystroke made by the user, including letters, numbers, symbols, and special keys. This allows for comprehensive logging of user input.

Logs keystrokes to a file:
All captured keystrokes are saved to a log file, typically named keylog.txt. This file can be easily accessed and analyzed to review the captured keystrokes. The log file is updated in real-time as new keystrokes are detected.

Runs in the background:
The keylogger runs silently in the background, without disrupting the user's activities. It continuously monitors and logs keystrokes without displaying any visible windows or notifications. This makes it unobtrusive and suitable for long-term monitoring.

Cross-platform support (Windows, macOS, Linux):
The keylogger is designed to be cross-platform, meaning it can run on various operating systems including Windows, macOS, and Linux. This flexibility allows users to deploy and use the keylogger on different systems without requiring modifications to the code.

**Detailed Feature Breakdown:**

Captures all keystrokes:

Records letters (both uppercase and lowercase).
Captures special characters (e.g., !, @, #, etc.).
Logs function keys (e.g., F1, F2, etc.).
Monitors control keys (e.g., Shift, Ctrl, Alt, etc.).
Recognizes navigation keys (e.g., Arrow keys, Home, End, etc.).
Logs keystrokes to a file:

Creates or appends to a log file named keylog.txt in the same directory as the script.
Formats the log file to include each keystroke in a readable format.
Handles special keys and control characters appropriately to ensure the log file remains clear and useful.
Runs in the background:

Utilizes the pynput library's listener mechanism to detect keystrokes without needing a visible application window.
Continues running until manually stopped or a predefined exit condition is met (e.g., pressing the Esc key).
Minimal resource usage ensures it does not impact system performance significantly.
Cross-platform support:

Leverages the pynput library, which abstracts away the differences between operating systems, providing a consistent API for keylogging.
Tested and confirmed to work on major operating systems, making it versatile for different environments.
Simple installation process using common Python package management tools like pip.
