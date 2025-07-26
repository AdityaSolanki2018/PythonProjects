# 🔤 NATO Phonetic Alphabet Translator

This Python program converts a user-inputted word into its NATO phonetic alphabet equivalent using the pandas library.

#🧠 Example
Input: 
Enter a word: Chat
Output:
['Charlie', 'Hotel', 'Alfa', 'Tango']

# 📁 Files
.
├── main.py                        # Your main script
└── nato_phonetic_alphabet.csv    # CSV file with letter-code mappings

Sample contents of nato_phonetic_alphabet.csv:
| letter | code    |
| ------ | ------- |
| A      | Alfa    |
| B      | Bravo   |
| C      | Charlie |
| ...    | ...     |

# 📦 Requirements

-Python 3.x
-pandas library

Install the required library (if not already installed):
pip install pandas

# ▶️ How to Run
1. Make sure nato_phonetic_alphabet.csv is in the same directory as your script.

2. Run the script:

python main.py

3. Enter a word when prompted, and you'll receive its phonetic equivalent.

# 🔧 How It Works
- Reads data from nato_phonetic_alphabet.csv using pandas.

- Creates a dictionary like {"A": "Alfa", "B": "Bravo", ...}.

- Accepts a word input from the user.

- Translates each letter into its phonetic code using the dictionary.

- Outputs the result as a list of phonetic words.

# 🚀 Possible Enhancements
- Handle invalid characters gracefully (like digits or special symbols).

- Add GUI using Tkinter or Gradio.

- Build a web version using Flask or Streamlit.

# 👨‍💻 Author
Aditya Solanki
📍 Python & Automation Enthusiast
📆 Part of my #100DaysOfCode challenge!


