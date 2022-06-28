import random
import string
#from tkinter.messagebox import YES

def main(): 
    #start the game by asking if user wants to be the guesser
    guessWho =str(input("Let's play the number guessing game.  Do want to be the guesser? "))
    #if they anser yes, run guesser function
    if guessWho == 'yes':  
        guesser() 
    #if they answer no, run guessy function
    elif guessWho == 'no':
        print('Ok, I am the guesser. Think of a number between 1 and 100. ')
        firstguess = 50
        guessy(firstguess)
    #otherwise try again
    else:
        print( "I didn't understand. Try again. ")
        main()

#code for user as guesser 
def guesser():
    print('Ok, you are the guesser. I am thinking a number between 1 and 100. ')
    number = random.randint(1, 100)
    guess=200
    while (guess != number): #make sure nubmer is valid
        try:
            guess=int(input("Guess a number. "))
        except ValueError:
            print("The input was not a valid integer.")

        if guess > 100 or guess < 0:
            print( "That's not between 1 and 100! Try again. ")
        elif guess > number:
            print("Lower! Try agin. ")
        elif guess < number:
            print("Higher! Try agin. ")
        else:
            again = str(input("You guessed it! Do you want to play again? "))
            if again == 'yes':
                main()
            else:
                print("Bye")

#code for user as guessy
def guessy(guess):
    re = 'no'
    high=100
    low=1
    while(re != 'yes'):
        re=input("is the number " + str(guess) + ". Please respond with yes, higher, or lower. ")
        if re == "yes":
            again = str(input("Yeah! Do you want to play again? "))
            if again == 'yes':
                main()
            else:
                print("Bye")
        elif re == "higher":
            if low < guess:
                low = guess
            guess = int((high-low)/2+low)
        elif re == "lower":
            if high > guess:
                high = guess
            guess = int((high-low)/2+low)



main()