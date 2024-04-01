"""A code guessing game to determine the number arrangement of three digits"""

import random

Num_Digits=3
Max_Guesses = 10

def main():
    print(f"""'Bagels, a deductive logic game.
     By Al Sweigart al@inventwithpython.com
    I am thinking of a {Num_Digits}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:    That means:
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
    Bagels       No digit is correct.
    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico""")
    while True:
        secretNum= get_secret_num()
        print('I have thought of a number.')
        print(f'You have {Max_Guesses} guesses to get it.')
    
        num_guesses =1
        while num_guesses <=Max_Guesses:
            guess=''
            #keeps loop going until they enter a valid guess:
            while len(guess) != Num_Digits or not guess.isdecimal():
                print(f'Guess #{num_guesses}:')
                guess=input('>')

                clues=get_clues(guess, secretNum)
                print(clues)
                num_guesses +=1

                if guess==secretNum:
                    return'you guessed correctly' 
                    break #if their guess is correct it breaks out of the loop here.
                if num_guesses > Max_Guesses:
                    print('You ran out of guesses.')
                    print(f'The answer was {secretNum}')

        #Ask if the player wants to play again.
        print('Do you want to play again?(yes or no)')
        if not input('>').lower().startswith('y'):
            break
        print('Thanks for playing!')
            
def get_secret_num():
    """Return a string made up of  unique random digits"""
    numbers=list('0123456789')
    random.shuffle(numbers)

    #Get the first digits in the list for the secret number

    secretNum=''
    for i in range(Num_Digits):
        secretNum += str(numbers[i])
    return secretNum

def get_clues(guess, secreNum):
    if guess== secreNum:
        return'You got it!'
    
    clues=[]

    for i in range(len(guess)):
        if guess[i]==secreNum[i]:
            clues.append('Fermi')
        elif guess[i] in secreNum:
            clues.append('Pico')

    if len(clues)== 0:
        return 'Bagels'
    else:
        clues.sort()
        return''.join(clues)
    
if __name__=='__main__':
    main()