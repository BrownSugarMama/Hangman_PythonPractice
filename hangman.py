msg = 'Hello World'
print(msg)

    # Get a random word : List of words that will be picked for the player


import random 

    # Small sample list of words for the game: array
words = ['general, assembly, developer, engineer, immersive, fifteen, washington,']

#lives remaining
lives_left = ''
#letters guessed
letters_guessed = ''

#random.randint allows code to return integers -- https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.randint.html
def chooseWord () :
    letter = random.randint(0, len(words)-1)
    return words[letter]

print(chooseWord()) # words printed into console

# Getting the game to play (play function)

def play():
    word = chooseWord()
    #if/else (conditional should work here, similar to simon game)
    guess = player_guess
    if word_guess (guess, word):
        print ('You won the game! Great Job!')
        break
    else
        != word_guess (gues, word): 
        print ('Oh No! Hangman! Better luck next time')
        print ('Would you like ot play again? Y/N')
        

