import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}! "))
        if guess < random_number:
            print("Try a higher number!")
        elif guess > random_number:
            print("Try a lower number!")
    print("Congratulations, you have guessed the number!")
    
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #Could also be "high"
        feedback = input(f"Is {guess} too high(H), too low(L), or correct(C)?").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print("The computer have guessed your number!")

#Unccomment the corresponding code to play the guessing game

#Defining the Range
range = 10  #Change the value as your wish (integer).

#User Guessing the Number
#guess(range)

#Computer Guessing the Number
#computer_guess(range)
