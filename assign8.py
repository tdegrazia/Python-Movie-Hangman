# Tanner DeGrazia, CS051A Assignment 8, April 2nd, 2023
# This program looks to play hangman from inside one class


from movies import *
import random

class LabeledExample:
    # creates example class
    def __init__(self, line_string, bool):
        """
        establishes a line of string and T/F as a variable for the rest of the class
        :param line_string: A string line that represents text
        :param bool: A boolean, either True or False
        """
        # Constructor function
        self.boolean = bool
        self.line = line_string

    def is_positive(self):
        """
        determines if the example is positive or not
        :return: (boolean) T/F depending on positive or negative
        """
        return self.boolean

    def lowercase(self):
        """
        Changes the example to lowercase
        :return: none
        """
        self.line = self.line.lower()

    def get_words(self):
        """
        gives the list of words in example
        :return: a list of words
        """
        word_list = []
        # Creates an empty list to append each split word to
        split_string = self.line.split(" ")
        # Splits the words in line at the spaces
        for words in split_string:
            word_list.append(words)
        return word_list

    def contains_word(self, word):
        """
        Tests if a certain word exists in the text line
        :param word: word to be tested in line (string)
        :return: boolean (T/F)
        """
        if word in self.line:
            return True
        else:
            return False

    def __str__(self):
        """
        Gives representation of example
        :return: final answer in string format
        """
        if self.boolean:
            return self.line + ":    positive"
        else:
            return self.line + ":    negative"


# ----------------
# Hangman Class

class Hangman:
    MAX_INCORRECT_GUESSES = 8

    def __init__(self, movie_title):
        """
        Establishes three variables to be used universally in the class
        :param movie_title: string of the movie's title to be made into a variable
        """

        self.movie = movie_title
        self.current = []
        # universal variable of an empty list
        self.guessed = []
        # universal variable of an empty list
        self.incorrect_guesses = []  # New list for incorrect guesses

        for i in movie_title:
            if i == " ":
                self.current.append(i)
                # appends space to the list of dashes
            else:
                self.current.append("-")
                # appends dash to the list of dashes representing movie title

    def current_state_to_string(self):
        """
        converts whatever type the game is to a string
        :return: a string of words
        """
        string_words = ' '.join(self.current)
        return string_words

    def guess(self, letter):
        """
        Function determines if the letter guessed is in the movie name
        :param letter: represents the character guessed
        :return: A string with the letter guessed now in it, if it is correct
        """
        letter = letter.lower()

        if letter not in self.guessed:
            self.guessed.append(letter)

            if letter not in self.movie:
                # If the letter is not in the movie title, increment the incorrect guesses counter
                self.incorrect_guesses.append(letter)
                if len(self.incorrect_guesses) >= self.MAX_INCORRECT_GUESSES:
                    # Check if the player has exceeded the maximum allowed incorrect guesses
                    print("___________________")
                    print("You lose! Too many incorrect guesses.")
                    print("The movie was: " + self.movie)
                    exit()  # Terminate the program

            for i in range(len(self.movie)):
                if letter == self.movie[i]:
                    self.current[i] = letter.upper()

        return self.current

    def display_incorrect_guesses(self):
        """
        Displays the list of incorrect guesses
        :return: a string containing the incorrect guesses
        """
        return "Incorrect guesses: " + ' '.join(self.incorrect_guesses)

        # 8 wrong = loss

    def has_won(self):
        """
        determines if game has been won or not
        :return: boolean (T/F)
        """
        if "-" not in self.current:
            return True
        else:
            return False

    def __str__(self):
        """
        Gives a representation of the guessed letters and the movie name
        :return: a string that plays into the final game
        """
        return (
                "\n___________________\n" +
                "Guessed letters: " + str(self.guessed) + "\n" +
                self.display_incorrect_guesses() + "\n" +  # Include incorrect guesses
                "Movie: " + self.current_state_to_string()
        )


def play_hangman():
    """
    Play the hangman game.    
    """
    # pick a movie for this game
    (movie, description, year) = random.choice(get_movies())

    hangman = Hangman(movie)

    print("*** Movie Hangman ***")
    print("Year: " + str(year))
    print(description)

    # keep playing until they've won
    while not hangman.has_won():
        # print out the state of the game
        print(hangman)

        letter = input("Guess a letter: ")
        letter = letter.lower()

        # update the state of the game based on the letter
        hangman.guess(letter)

    print("___________________")
    print("You win!")
    print("The movie was: " + movie)
