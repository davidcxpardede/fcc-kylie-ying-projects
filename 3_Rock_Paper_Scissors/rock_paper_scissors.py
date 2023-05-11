import random

def play():
    user = input("What is your choice? 'R' for Rock, 'P' for Paper, and 'S' for Scissors ")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return "It's a tie."
    
    if is_win(user, computer):
        return "You won!"
    
    return "You lost!"

def is_win(player, opponent):
    #Return true if Player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())