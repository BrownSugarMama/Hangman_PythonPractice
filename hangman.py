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
    letter_position = random.randint(0, len(words) - 2)
    return words[letter_position]

print(choose_word()) # single random word printed into console

# Getting the game to play (play function)

def play():
    word = choose_word()
    while True:           
        guess = player_guess (word)
    # if/else (conditional should work here, similar to simon game)
          if word_guess = (guess, word):
        print ('You won the game! Great Job!')
        break
    else
        != word_guess (guess, word): 
        print ('Oh No! Hangman! Better luck next time')
        print ('Would you like ot play again? Y/N')
        
# Player guess function
def player_guess(word):
    word_blanks(word)
    print ('Guesses Remaining: ' + str(lives_left))
    guess = input('guess the a letter or word?')
    return guess

def word_blanks(word):
    show_word = ''
    for letter in word:
        if letters_guessed.find(letter) > -1:
            #if letter is correct
            show_word = show_word + letter
        else :
            #if letter is incorrect
            show_word = show_word + '--'
    print(show_word)
