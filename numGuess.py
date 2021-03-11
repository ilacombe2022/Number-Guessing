from random import randrange

def userChoice():
    confirm = input("Would you like to play? Press p to continue\n")
    if confirm == 'p' or confirm == 'P':
        return confirm
    else:
        print("Invalid choice! Try again\n")
        userChoice()

def playGame():
    startNum = 0
    endNum = 0
    randomNum = 0

    startNum = int(input("Pick a number: "))
    print("Confirmed! You have chosen %d\n" % startNum)
    endNum = int(input("Pick a number higher than your first number: "))
    print("Confirmed! You have chose %d\n" % endNum)

    if endNum > startNum:
        randomNum = randrange(startNum, endNum)
        getNumGuess = guess()
        matchNum(randomNum, getNumGuess, startNum, endNum)
    else:
        print("This number is less than or equal to your first one!\n")
        return

def guess():

    numOfGuess = int(input("How many guess would you like?[3-10]: "))

    if numOfGuess >= 3 and numOfGuess <= 10:
        print("You have chosen to have %d guesses. Valid!\n" % numOfGuess)
        return numOfGuess
    else:
        print("You have chosen to have %d guesses. Invalid!\n" % numOfGuess)
        guess()

def matchNum(correctNum, guesses, first, last):

    yourGuess = 0

    while guesses != 0:
        print("You have %d guess(es) left" % guesses)
        yourGuess = int(input("Choose a number between %d and %d: " % (first, last)))
        print("\n")

        if yourGuess > correctNum and yourGuess < last and guesses != 0:
            print("Your guess is greater than the number!\n")
        elif yourGuess < correctNum and yourGuess > first and guesses != 0:
            print("Your guess is less than the number!\n")
        elif yourGuess > last and guesses != 0:
            print("Your number is invalid! It is greater than %d!\n" % last)
        elif yourGuess < first and guesses != 0:
            print("Your number is invalid! It is less than %d!\n" % first)
        elif yourGuess == correctNum and guesses != 0:
            print("YOU GUESSED THE RIGHT NUMBER WITH %d GUESS(ES) LEFT!!!\n" % (guesses - 1))
            continueGame()
        guesses = guesses - 1

    if guesses == 0:
        print("YOU'VE RAN OUT OF GUESSES! The number was %d\n" % correctNum)
        continueGame()

def continueGame():
    choice = input("Would you like to continue?(y/n): ")
    print("\n")
    while choice == 'y' or choice == 'Y' or choice == 'n' or choice == 'N':
        if choice == 'y' or choice == 'Y':
            playGame()
        elif choice == 'n' or choice == 'N':
            print("Thanks for playing!")
            exit()

    print("Invalid Choice!\n")
    continueGame()

print("Welcome to the Number Guessing Game:")
print("Created By: Isaac Lacombe")

userChoice()
playGame()