
print("Hello, welcome to Age Guesser! Let's guess your age.")
name = input("What is your name? ")

guessed = False

while not guessed:
    age = random.randint(15,30)
    
    answer = input("Are you " + str(age) + "? (y/n): ")
    
    if answer == 'y':
        print("YAY! " + name + " is " + str(age) + " years old.")
        guessed = True

    else:
        print("Rats.")