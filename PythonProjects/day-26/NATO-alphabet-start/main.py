import pandas

# Create a dictionary in this format:

alpha_data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_alph = {row.letter:row.code for (index, row) in alpha_data.iterrows()}
print(phonetic_alph)

# Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic_alphabets():
    word = input("Enter a word to generate Phonetic Alphabet: ").upper()
    try:
        word_phonetic_alph = [phonetic_alph[alphabet] for alphabet in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic_alphabets()
    else:
        print(word_phonetic_alph)


generate_phonetic_alphabets()

