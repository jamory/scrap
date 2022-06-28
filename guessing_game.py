import random

def main(): 
    #start the game by asking if user wants to be the guesser
    guessWho =str(input("Let's play the number guessing game.  Do want to be the guesser? "))
    #if they anser yes, run guesser function
    if guessWho == 'y':  
        guesser() 
 
def guesser():
    print('Ok, you are the guesser. I am thinking a number between 1 and 100. ')
    number = random.randint(1, 100)
    guess=200
    while (guess != number):
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
            if again == 'y':
                main()
            else:
                print("Bye")

#def guessy():
    

main()