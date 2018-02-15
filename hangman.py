msg = 'Hello World'
print(msg)

    # Get a random word : List of words that will be picked for the player


import random 

    # Small sample list of words for the game: array
words = ['general', 'assembly', 'developer', 'engineer', 'immersive', 'fifteen', 'washington',]
#lives remaining
lives_left = 5
#letters guessed
letters_guessed = ''

def choose_word () :
    letter = random.randint(0, len(words) - 2)
    return words[letter]

print(choose_word()) # single random word printed into console

# Getting the game to play (play function)

def play():
    word = choose_word()
    print (word())
    #if/else (conditional should work here, similar to simon game)
    # guess = player_guess
    # if word_guess (guess, word):
    #     print ('You won the game! Great Job!')
    #     break
    # else
    #     != word_guess (gues, word): 
    #     print ('Oh No! Hangman! Better luck next time')
    #     print ('Would you like ot play again? Y/N')
        

