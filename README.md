[README (6).md](https://github.com/user-attachments/files/32891893/README.6.md)
# 📔 Personal Journal Manager

A simple **Python-based Personal Journal Manager** that lets the user add, view, search, and delete journal entries. 🐍✨

## 📌 Project Information

- **Project Name:** Personal Journal Manager
- **Language:** Python 🐍
- **Storage File:** `journal.txt`
- **Main Project File:** `PROJECT 6(1).PY`
- **Purpose:** Manage personal journal entries using a text file. 📖

## 🚀 Features

1. ➕ **Add a New Entry**  
   Adds a journal entry with the current date and time.

2. 📖 **View All Entries**  
   Displays all saved journal entries from `journal.txt`.

3. 🔍 **Search for an Entry**  
   Searches journal entries using a keyword or date.

4. 🗑️ **Delete All Entries**  
   Deletes the journal file after confirmation.

5. 🚪 **Exit**  
   Closes the Personal Journal Manager.

## 🛠️ Python Concepts Used

- `import os` for checking and deleting the journal file.
- `import datetime` for adding date and time to entries.
- Functions such as `add_entry()`, `view_entries()`, `search_entries()`, and `delete_all_entries()`.
- File handling with `open()`.
- `while True` loop for the main menu.
- `if / elif / else` conditions for menu selection.
- String methods such as `.lower()`, `.strip()`, and `.split()`.
- Exception-free file existence checks using `os.path.exists()` and `os.path.getsize()`.

## 📂 How the Program Works

The program first displays a menu with five options. The user enters a menu number, and the corresponding function is executed. Journal entries are stored in `journal.txt` with a timestamp.

Example entry format:

```text
[2026-10-01 12:09:00]
rutvik
```

The program continues showing the menu until the user selects **5. Exit**. 👋

## 🖥️ Screenshots

### 1️⃣ Add Entry and View Entries

![Add Entry and View Entries](screenshot-1.png)

### 2️⃣ Search and Exit

![Search and Exit](screenshot-2.png)

## ▶️ How to Run

1. Install Python 3.
2. Keep `PROJECT 6(1).PY` in your project folder.
3. Open the file in VS Code, IDLE, or another Python editor.
4. Run the program.
5. Select an option from the menu. 🎯

## 📝 Example Menu

```text
Welcome to Personal Journal Manager!
Please select an option:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
```

## 📄 Files in This Project

| File | Description |
|---|---|
| `PROJECT 6(1).PY` | Main Python program 🐍 |
| `journal.txt` | Stores journal entries when created 📔 |
| `screenshot-1.png` | Program output screenshot 1 🖼️ |
| `screenshot-2.png` | Program output screenshot 2 🖼️ |
| `README.md` | Project documentation 📚 |

## 👨‍💻 Project Summary

This project demonstrates basic **Python functions, loops, conditions, file handling, strings, and date/time handling** through a practical Personal Journal Manager. 🚀🐍

---

⭐ **Personal Journal Manager — Simple, Useful & Easy to Understand!**
