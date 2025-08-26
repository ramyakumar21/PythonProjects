import pandas

# Create a dictionary in this format:

alpha_data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_alph = {row.letter:row.code for (index, row) in alpha_data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word to generate Phonetic Alphabet:").upper()

word_phonetic_alph = [phonetic_alph[alphabet] for alphabet in word]

print(word_phonetic_alph)

