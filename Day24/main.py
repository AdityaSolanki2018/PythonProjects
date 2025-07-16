# This is a sample Python script.
PLACEHOLDER = "[name]"


with open("./PythonProjects/Day24/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)
with open("./PythonProjects/Day24/Input/Letters/starting_letter.txt") as letter_template:
    letter = letter_template.read()
    for name in names:
        final_letter = letter.replace(PLACEHOLDER,name.strip())
        with open(f"./PythonProjects/Day24/Output/ReadyToSend/letter_for_{name.strip()}.txt",mode="w") as readyLetter:
            readyLetter.write(final_letter)
            print(f"Letter for {name.strip()} created.")
