print("Hello and welcome to Madlibs!")
print("You are going to make your story based on data that you will be asked to input.")

name = input("What is your name? ")
age = input("How old are you (in years)? ")

while True:
    gender = input("What is your gender (male or female)? ")
    if str(gender.lower()) == "male":
        pron = "he"         #Pronoun
        obj_pron = "him"    #Objective Pronoun
        psv_pron = "his"    #Possessive Pronoun
        prs_pron = "man"    #Personal Pronoun
        break
    elif str(gender.lower()) == "female":
        pron = "she"        #Pronoun
        obj_pron = "her"    #Objective Pronoun
        psv_pron = "her"    #Possessive Pronoun
        prs_pron = "woman"    #Personal Pronoun
        break
    else:
        print("Please enter a valid gender.")

hobby = input("What is your hobby? ")
city = input("In which city do you live? ")
country = input("In which country do you live? ")

routine1 = input("What do you do first in the morning? ")
routine2 = input("What do you do after that? ")
routine3 = input("What do you do before bed? ")

trait = input("What do your friends like about you the most? ")
motto = input("What is your motto? ")
idol = input("Who is your idol? ")
dream = input("What do you want to be? ")
reason = input("Why do you want to be such? ")

print("Thanks for inputting your data!")
choice = input("Please hit enter to see your story!")
print("\n\n\n")

print(f"THE STORY OF {name.upper()}\n\n")
print(f"There lives a {prs_pron} named {name}.")
print(f"Today, {pron} is {age} years old.")
print(f"{name} lived in {city}, {country},")
print(f"As a hobby, {pron} likes to {hobby}.\n\n")

print(f"Every morning, {name} starts {psv_pron} by {routine1}.")
print(f"Then, {pron} prepares himself and go to {routine2}.")
print(f"{name} closes {psv_pron} day by {routine3} before finally going to bed.")

print(f"{name} is a very {trait} {prs_pron}. That's why all {psv_pron} likes {obj_pron}.")
print(f"{name} believes that '{motto}', and {pron} lives up to that principle.")
print(f"{name} dreams to be a {dream}, and {pron} is inspired by {idol}.")
print(f"When facing obstacles, {pron} always remember his true reason and main objective, which is {reason}.")