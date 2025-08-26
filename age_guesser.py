import random

print()
print("~~ Hello, welcome to Age Guesser! Let's guess your age. ~~")
print()

name = input("-- What is your name? _")

guessed = False

lower = 15
upper = 30

while not guessed:
    age = random.randint(lower,upper)
    
    answer = input(f"Are you {age}? (y/n): _")
    
    if answer == 'y':
        print(f"YAY! {name} is {age} years old.")
        guessed = True

    else:
        print("Rats.")
        feedback = input(f"-- Are you older or younger than {age}? (older/younger): _")

        if feedback == 'older':
            lower = age + 1
        elif feedback == 'younger':
            upper = age - 1