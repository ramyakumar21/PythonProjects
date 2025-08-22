# Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

TO_REPLACE = "[name]"

with open("Input/Letters/starting_letter.txt", mode ="r") as starting_letter:
    sample = starting_letter.read()
#print(starting_letter)

with open("Input/Names/invited_names.txt", mode ="r") as replace_name_list:
    names_list = replace_name_list.readlines()
#print(replace_name)

for name in names_list:
    replace = sample.replace(TO_REPLACE, name.strip())
    file = open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w")
    file.write(replace)









