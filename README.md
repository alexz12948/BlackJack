# BlackJack

This is a program that allows the user to play a game of virtual BlackJack
against a computer. I included all of the testing files as well as the modules
in this folder.

## How to Run

python3 play_game.py

### Descriptions of Files
Note: every module has an associated test file, named test_moduleName.py

##### Modules for the Deck of Cards
card.py - A class that represents one card, and has getter functions as well as a __str__ function to be able to print out itself
deck.py - A class that represents the entire deck of cards, including the initialization of the full deck as well as a function that deals cards to the players

##### Modules for the Players
person.py - A superclass that represents a player in the game and contains functions that allow for calculations of totals and general game functions
dealer.py - A subclass of Person, which contains functions specific to the dealer of BlackJack
user.py - A subclass of Person, which contains functions that allow the user to play the game properly

##### Modules for Testing
unittest.sh - A script that runs all of the testing files for each module and prints out an error message if any of the tests fails
test_* - The associated testing file for a module
