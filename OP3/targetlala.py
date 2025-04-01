"""
Target game OOP implementation
"""

import random


class Word:
    """
    Represents a word used in the Target game.
    """

    def __init__(self, word: str):
        """
        Initializes a Word object.

        Args:
            word (str): The word to be stored.

        >>> word1 = Word("FlowEr ")
        >>> word2 = Word("meadow")
        >>> word3 = Word("sunsEt")
        >>> words_lst = [word1, word2, word3]
        >>> print(words_lst)
        [flower, meadow, sunset]
        """
        self.word = word.strip().strip("\n").lower()

    def __repr__(self):
        """
        Returns a string representation of the word.

        Returns:
            str: The word in lowercase.

        >>> word1 = Word("FlowEr ")
        >>> repr(word1)
        'flower'
        """
        return f"{self.word}"

    def __eq__(self, other_word):
        """
        Compares two Word objects for equality.

        Args:
            other_word (Word): Another Word object.

        Returns:
            bool: True if both words are the same, False otherwise.
        """
        if isinstance(other_word, Word):
            return self.word == other_word.word
        return False

    def is_valid(self, board):
        """
        Checks if the word is valid according to the board rules.

        Args:
            board (Board): The game board.

        Returns:
            bool: True if the word is valid, False otherwise.
        """
        if sum(1 for j in board.grid for i in j if i.islower()) or len(self.word) < 4:
            return False
        letters = [let.lower() for row in board.grid for let in row]
        for ch in self.word:
            if ch not in letters:
                return False
        for ch in self.word:
            if self.word.count(ch) > letters.count(ch):
                return False
        if letters[4] not in self.word:
            return False
        return True




class Board:
    """
    Represents the game board.
    """
    def __init__(self, grid=None):
        """
        Initializes the board with a predefined grid
        or generates a random one.

        Args:
            grid (list[list[str]], optional):
            A 3x3 list of letters. Defaults to None. 
        """
        if grid is None:
            self.grid = self.generate_grid()
        else:
            self.grid = grid

    def __str__(self):
        """
        Returns a string representation of the board.

        Returns:
            str: The formatted board as a string.
        """
        res_str = "\n".join("".join(row) for row in self.grid)
        return f"Your board is:\n{res_str}"

    @staticmethod
    def generate_grid():
        """
        Generates a random 3x3 grid of letters with vowels and consonants.

        Returns:
            list[list[str]]: A 3x3 list of letters.
        """
        letters = []
        for _ in range(3):
            letters.append(random.choice('AEIOU'))
        for _ in range(6):
            letters.append(random.choice('BCDFGHGKLMNPQRSTVWXYZ'))

        random.shuffle(letters)

        result = []
        for i in range(3):
            result.append(letters[i * 3:i * 3 + 3])
        return result

    def get_words(self, filename):
        """
        Retrieves all valid words from a dictionary
        file that can be formed using the board's letters.

        Args:
            filename (str): The dictionary file containing words.

        Returns:
            list[Word]: A list of valid Word objects.
        """
        letters = [let.lower() for row in self.grid for let in row]
        good_words = []
        with open(filename, 'r', encoding='utf-8') as words:
            list_words = words.readlines()
            for line in list_words:
                letters_copy = letters.copy()
                word = (line[:-1]).lower()
                if (len(word)>=4) and (letters[4] in word):
                    for char in word:
                        if char not in letters_copy:
                            break
                        try:
                            letters_copy.remove(char)
                        except ValueError:
                            break
                    else:
                        good_words.append(Word(word))
        return good_words



class TargetGame:
    """
    Implements the Target word game logic.
    """
    def __init__(self, filename, board=None, user_words=None):
        """
        Initializes the game with a word list, board, and user inputs.

        Args:
            filename (str): Dictionary file.
            board (list[list[str]], optional):A 3x3 letter grid. Defaults to None.
            user_words (list[str], optional): A list of words input by the user. Defaults to None.
        """
        self.filename = filename

        if board is None:
            self.board = Board(Board.generate_grid())
        else:
            self.board = Board(board)


        self.__user_words = [Word(w) for w in self.get_user_words(user_words)]

        self.__possible_words = self.board.get_words(filename)
        self.__correct_user_words = [w for w in self.__user_words if w.is_valid(self.board)]


    def __str__(self):
        """
        Returns a summary of the game results.

        Returns:
            str: The formatted game results.
        """
        return f"---------Game results---------:\nThe list of your words is:\n\
{self.user_words}\nThe list of your correct words:\n{self.correct_user_words}\n\
The number of possible words: {len(self.__possible_words)}\nYou guess \
{(len(self.correct_user_words)/len(self.__possible_words))*100:.0f}% of possible words."

    @property
    def correct_user_words(self):
        """
        Returns the list of correctly guessed words.

        Returns:
            list[Word]: The list of correct words.
        """
        return self.__correct_user_words

    @property
    def user_words(self):
        """
        Returns the list of user-entered words.

        Returns:
            list[Word]: The list of user words.
        """
        return self.__user_words

    @user_words.setter
    def user_words(self, new_words):
        """
        Sets a new list of user words.

        Args:
            new_words (list[Word]): The new list of words.
        """
        self.__user_words = list(map(Word, new_words))
        self.__correct_user_words = []
        for word in self.__user_words:
            if word.is_valid(self.board):
                self.__correct_user_words.append(word)


    def get_user_words(self, words):
        """
        Reads user words from input until EOF is encountered.
        """
        print(f"{str(self.board)}Please, suggest your words.\n\
When you finished, hit: *nix: Ctrl-D, Windows: Ctrl-Z+Return")
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

if __name__ == "__main__":
    # my_board = Board([['E', 'S', 'Z'], ['Y', 'C', 'I'], ['D', 'P', 'Y']])
    # my_board = Board()
    # print(str(my_board))
    # print(my_board)
    game = TargetGame('en.txt', [['E', 'S', 'Z'], ['Y', 'C', 'I'], ['D', 'P', 'Y']], ['Dice', 'spIcy', 'float'])
    # game.get_user_words(['so'])
    # game = TargetGame('en.txt')
    # print(game.board)
    word1 = Word('dice')
    print(word1.is_valid(Board([['E', 'S', 'Z'], ['Y', 'c', 'I'], ['D', 'P', 'Y']])))
    print(word1.is_valid(Board([['E', 'S', 'Z'], ['Y', 'C', 'I'], ['D', 'P', 'Y']])))
    print(game)
