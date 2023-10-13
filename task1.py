#!python3

'''
Create a number guessing game
There is a limit of 10 guesses
The program will ask the user to enter an integer from 1 to 100
The program will then tell the user if the number is too high, too low or correct.
If the number is correct, the program will end
If the 10 guesses are used up, the program will say that the user has lost
'''
number = 36
for i in range(1,11):
    guess = int(input("Guess the 1-100 number: "))
    if guess > number:
        print(f"{guess} is too high")

    if guess < number:
        print(f"{guess} is too low")

    if guess == number:
        print(f"{guess} is correct")
        break
else:
    print("all 10 guesses are up")


    
