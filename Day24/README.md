# 📩 Automated Letter Generator (Day 24 – 100 Days of Python)

This project automatically generates **customized letters** for a list of recipients using a text-based template.

It’s a great example of **file handling**, **string manipulation**, and **automating repetitive tasks** with Python.

---

## 🧠 What I Learned

- Reading and writing files with `with open(...)` syntax
- Processing a list of names from a `.txt` file
- Replacing placeholders in a template
- Dynamically creating personalized files with clean filenames
- Automating repetitive document generation tasks

---

## 🛠️ Tech Used

- Python 3.x
- Basic file operations (`open`, `read`, `write`)
- String replacement with `replace()`
- File path navigation

---

## 📂 Folder Structure

📁 Day24_CustomLetterGenerator/
   ├── main.py
   ├── Input/
   │ ├── Names/
   │ │ └── invited_names.txt
   │ └── Letters/
   │ └── starting_letter.txt
   ├── Output/
   │ └── ReadyToSend/
   │ └── letter_for_<Name>.txt
   └── README.md

## ▶️ How It Works

1. **Template Letter:**  
   `starting_letter.txt` contains a letter with a placeholder (`[name]` or similar).

2. **Recipient List:**  
   `invited_names.txt` has one name per line.

3. **The Script:**
   - Reads all names.
   - Replaces the placeholder with each name.
   - Saves the output to a new text file in `Output/ReadyToSend`.

---

## ✅ Example

Dear [name],
You are invited to the annual celebration!
Regards,
Team Python

**Output for "Alice":**

Dear Alice,
You are invited to the annual celebration!
Regards,
Team Python


## 💡 Improvements to Try Later

- Add email sending via `smtplib`
- Allow custom placeholders like `[name]`, `[event]`, `[date]`
- Convert to a CLI tool or Streamlit app

---

> Built with Python, purpose, and personalization 🧠💌
