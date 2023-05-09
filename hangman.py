import random
import string

words = ["horas", "mejuahjuah", "njuahjuah", "yaahowu", "ahoi"]

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)    # Letters in the Word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #What the User has Guessed
    
    #Getting User Input
    user_letter = input("Guess a letter: ").upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
    
    elif user_letter in used_letters:
        print("You have already used that character. Please try another letter.")
    else:
        print("Invalid character. Please try again.")

#user_input = input('Type something: ')
#print(user_input)

hangman()