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
    while len(word_letters) > 0:
        
        #Letters used
        print("You have used these letters: ", "".join(used_letters))
        
        #What the current word is (i.e. W _ R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", "".join(word_list))
        
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        
        elif user_letter in used_letters:
            print("You have already used that character. Please try another letter.")
        else:
            print("Invalid character. Please try again.")

    #Gets here when len(word_letter == 0)
#user_input = input('Type something: ')
#print(user_input)

hangman()