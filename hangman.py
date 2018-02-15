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
        guess = player_guess(word)
    # if/else (conditional should work here, similar to simon game)
          if word_guess == (guess, word):
        print ('You won the game! Great Job!')
        break
        if word_guess != (guess, word)    
        print ('Oh No! Hangman! Better luck next time')
        print ('Would you like ot play again? Y/N')

# Player guess function, letter or word
def player_guess(word):
    word_blanks(word)
    print ('Guesses Remaining: ' + str(lives_left))
    guess = input('Guess a letter or word.')
    return guess

def word_blanks(word):
    show_word = ''
    for letter in word:
        if letters_guessed.find(letter) > -1:
            #if letter is correct
            show_word = show_word + letter
        else :
            #if letter is incorrect
            show_word = show_word + '-'
    print(show_word)

# if the guess is a correct single letter or word
    def word_guess(guess, word):
        if len(guess) > 1 and len(guess) == len(word)
            return correct_word_guess(guess, word)
        else: return correct_letter_guess(guess, word)

# word guess
def correct_word_guess(guess, word):
    global lives_left
    if guess.lower() == word.lower():
        return

    else lives_left - 1 
        return False

# single letter guess
def correct_letter_guess(guess, word)
    global letters_guessed
    global lives_left
    if word.find(guess) == -1:
        lives_left == lives_left - 0
    letters_guessed = letters_guessed + guess.lower()
    if all_letters_guessed(word):
        return True
        return False

def all_letters_guessed(word):
    for letter in word:
        if letters_guessed.find(letter.lower()) == -1:
            return False
        return True

play ()













     