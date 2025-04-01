'''This module holds classes'''
import random


class Word:
    """
    Represents a word.

    """

    def __init__(self, word: str):
        """
        Initializer
        Args:
        word (str): The word to be stored.
        """
        self.word = word.strip().strip().lower()

    def __repr__(self):
        """
        Returns a string representation.
        """
        return self.word

    def __eq__(self, other_word):
        """
        Compares
        Args:
        other_word (type: Word): Word object.
        Returns:
        bool
        """
        return isinstance(other_word, Word) and self.word == other_word.word

    def is_valid(self, board):
        """
        Checks if the word is valid.
        Args:
        board (Board): The  board.
        Returns: bool
        """
        if len(self.word) < 4 or sum(1 for row in board.grid for letter in row if letter.islower()) > 0:
            return False
        letters = [letter.lower() for row in board.grid for letter in row]
        if self.word.count(letters[4]) == 0:
            return False
        for ch in self.word:
            if self.word.count(ch) > letters.count(ch):
                return False
        return all(ch in letters for ch in self.word)


class Board:
    """
    The board class.
    """
    def __init__(self, grid=None):
        """
        Initializer.
        Args:
        grid (type: list): letter list
        """
        self.grid = grid if grid is not None else self.generate_grid()

    def __str__(self) -> str:
        """
        Returns a string representation of the board
        Returns: str
        """
        res_str = "\n".join("".join(row) for row in self.grid)
        return f"Your board is:\n{res_str}"

    @staticmethod
    def generate_grid():
        """
        Generates grid of letters 
        Returns:
        list: a list of letters (3x3)
        """
        letters = [random.choice('AEIOU') for _ in range(3)] + \
                  [random.choice('BCDFGHJKLMNPQRSTVWXYZ') for _ in range(6)]
        random.shuffle(letters)

        return [letters[i * 3:(i + 1) * 3] for i in range(3)]

    def get_words(self, filename:str) -> list:
        """
        Gets words that are valid
        Args:
        filename (type:str): The dictionary file with words.
        Returns:
        list[Word]: A list of suitable Word objects.
        """
        board_letters = [char.lower() for row in self.grid for char in row]
        found_words = []

        with open(filename, 'r', encoding='utf-8') as file:
            for entry in file:
                word_candidate = entry.strip().lower()
                if len(word_candidate) >= 4 and board_letters[4] in word_candidate: 
                    temp_board_letters = board_letters[:]
                    is_valid_word = True 

                    for letter in word_candidate:
                        if letter in temp_board_letters:
                            temp_board_letters.remove(letter)
                        else:
                            is_valid_word = False
                            break

                    if is_valid_word:
                        found_words.append(Word(word_candidate))

        return found_words


class TargetGame:
    """
    Target class
    """
    def __init__(self, filename, board=None, user_words=None):
        """
        Initializer
        Args:
        filename (type: str): Dictionary file.
        board (type: list[list[str]], optional): A 3x3 letter grid. Defaults to None.
        user_words (type: list[str], optional): A list of words input by the user. Defaults to None.
        """
        self.filename = filename
        self.board = Board(board) if board is not None else Board()
        self.__user_words = [Word(w) for w in self.get_user_words(user_words)]
        self.__possible_words = self.board.get_words(filename)
        self.__correct_user_words = [w for w in self.__user_words if w.is_valid(self.board)]

    def __str__(self) -> str:
        """
        Returns a string representation with results
        """
        return f"---------Game results---------:\nThe list of your words is:\n\
{self.user_words}\nThe list of your correct words:\n{self.correct_user_words}\n\
The number of possible words: {len(self.__possible_words)}\nYou \
guess {(len(self.correct_user_words)/len(self.__possible_words))*100:.0f}% of possible words."

    @property
    def correct_user_words(self):
        """
        Returns the list of guessed words.
        Returns: list, the list of words that are correct
        """
        return self.__correct_user_words

    @property
    def user_words(self):
        """
        Returns the list of words from user
        """
        return self.__user_words

    @user_words.setter
    def user_words(self, new_words):
        """
        Sets a new list of user words.
        """
        self.__user_words = [Word(w) for w in new_words]
        self.__correct_user_words = [word for word in self.__user_words if word.is_valid(self.board)]

    def get_user_words(self, words):
        """
        Reads the words and checks for End of File error
        """
        print(f"{str(self.board)}\nPlease, suggest your words.\n"
              "When you finished, hit: *nix: Ctrl-D, Windows: Ctrl-Z+Return")
        if words is None:
            words_list = []
            while True:
                try:
                    word = input()
                    words_list.append(word)
                except EOFError:
                    break
            return words_list
        return words
