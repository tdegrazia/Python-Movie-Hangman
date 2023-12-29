# Movie Hangman Game
## Introduction
This Python program is a text-based Hangman game that revolves around guessing the titles of movies. The game is implemented within two classes: LabeledExample and Hangman. Additionally, there is a movies.py file that contains functions for retrieving movie data from a CSV file.

## Files
### hangman.py

This file contains the implementation of the Hangman game. The game is played by guessing letters to reveal the movie title. The player can win by correctly guessing the entire title or lose by exceeding the maximum allowed incorrect guesses.

### movies.py

This file includes functions for fetching movie data from a CSV file. The data includes movie titles, descriptions, and release years. The data is used in the Hangman game to randomly select a movie for each round.

### movie_info.csv

This CSV file contains movie data, such as titles, descriptions, and release years. It serves as the dataset for the Hangman game.

## How to Play
- Run the hangman.py script.
- Plug the play_hangman() function into the console to begin.
- The game will randomly select a movie for you to guess.
- Enter letters to guess the movie title.
- You have a maximum of 8 incorrect guesses. If exceeded, the game ends.
