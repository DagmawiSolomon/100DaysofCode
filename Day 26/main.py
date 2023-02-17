import pandas



nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alp = {row.letter: row.code for (index, row) in nato_phonetic_alphabet.iterrows()}


def generate_function():
    user_input = input("Enter a word: ")
    try:
        conv = [alp[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_function()
    else:
        print(conv)

generate_function()

