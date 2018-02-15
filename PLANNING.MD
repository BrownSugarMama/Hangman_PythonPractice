## PLANNING

) Install Python and Enviornment Setup
    - http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/
    - https://tutorial.djangogirls.org/en/python_installation/
    - $ brew install python3 
    OR  https://www.python.org/downloads/release/python-363/

) Install 'pip' command
    - sudo easy_install pip

) Install 'vitualenv'
    

) Verify Python is Install
    - $ python3
        Python 3.6.3 confirmed
    - http://docs.python.org/3.6/tutorial/

) Install Python Extension in VS Code

) Learning Python Basics
    - Integers, Strings, Lists, Variables, and Errors: 
      https://www.youtube.com/watch?v=MO63L4s-20U
    - Shannon Turner, Hear Me Code -- Python For Beginners

## HANGMAN GAME OVERVIEW + OUTLINE
=> Code the classic hangman game, where the computer selects a word randomly from a list, and the player guesses letters, with a limit for the number of wrong letter guesses, displayed somehow.  Correct guesses need to be indicated positionally.  For instance for the secret word "program", if the player has correctly guessed nothing, display underscores for all 7 letters:
_ _ _ _ _ _ _
Later if the user has correctly selected r, you should display something like
_ r _ _ r _ _
and then if g is selected,
_ r _ g r _ _
.... This display is the trickiest part of a basic version.
----------------------------------------------------------------
-- Make an 'Array' of words to be chosen from
-- Create a method for the letter the user choses to be returned
-- Create a method for the users lives to countdown with each incorrect answer
-- Create a function for the words and letters to be called
-- Create a 'Play Function'    

## RESOURCES
-- Difference b/t Funtions + Methods" 
   https://teamtreehouse.com/community/difference-between-functions-and-methods-in-python
-- TypeError: 'list' object is not callable in python
   https://stackoverflow.com/questions/31087111/typeerror-list-object-is-not-callable-in-python/3108715
-- Random choices from a list : https://anh.cs.luc.edu/150/hw/pythonProject.html#random
    > import random
    > aList = ['a', 'bb', 'ccc', 'dddd']
    > random.shuffle(aList)
    > aList
    ['ccc', 'a', 'dddd', 'bb']
    > entry = aList.pop()
    > entry
    'bb'
    > aList
    ['ccc', 'a', 'dddd']
So with shuffle and pop you can get random choices, and each time you pop from the list, you get a different element.
-- 

