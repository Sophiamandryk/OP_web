"""
Target game
"""

import random

# 1. Випадкове число
# number = random.randint(0, 1000)

# 2. Вибір випадкового елементу з масиву (1)
# names: list[str] = ["John", "Alice", "Jack"]
# random_name = random.choice(names)

# 3. Вибір декількох елементів з масиву
# print(random.sample(names, 2))

def generate_grid() -> list[list[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    vowels = ['A', 'E', 'I', 'O', 'U']
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',\
                   'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

    grid = []

    for _ in range(3):
        vowel = random.choice(vowels)
        consonants = random.sample(consonants, 2)
        letters = [vowel] + consonants
        random.shuffle(letters)
        grid.append(letters)

    return grid


def get_words(f: str, letters: list[str]) -> list[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    # if len(letters) % 2 == 0:
    #    return None
    # 1. Прочитати файл і отримати список слів
    # centered_letter = letters [len(letters) // 2]
    words_from_the_list = []

    letters = [lett.lower() for row in letters for lett in row]
    centered_letter = letters[4].lower()

    with open(f, 'r', encoding='utf-8') as file:
        # words = file.read().splitlines()


        for item in file:
            item = item.strip()
            item = item.lower()
            letters_copy = letters.copy()
            if len(item) >= 4 and centered_letter in item:
                for lett in item:
                    if lett not in letters_copy:
                        break
                    letters_copy.remove(lett)
                else:
                    words_from_the_list.append(item)
    return words_from_the_list




def get_user_words() -> list[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """

    words = []
    while True:
        try:
            user_input = input('Натистіть ctrl+d щоб вийти: \n>>')
        except EOFError:
            break
        if user_input:
            words.append(user_input)
    return words
# result = get_user_words()



def get_pure_user_words(user_words: list[str], letters: list[str],\
                         words_from_dict: list[str]) -> list[str]:
    """
    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    # dict_of_words = get_words('/Users/sofiyamandryk/Downloads/base.lst', letters)
    # user_words = get_user_words()
    centered_letter = letters [4]
    # counter = 0
    valid_words = []
    # glossary = get_words('/Users/sofiyamandryk/Desktop/OP/op2/en.txt', generate_grid())
    for word in user_words:
        if word.islower() and centered_letter in word and len(word) >= 4:
            # counter += 1
            if word not in words_from_dict:
                letters_copy = letters.copy()
                for lett in word:
                    if lett not in letters_copy:
                        break
                    letters_copy.remove(lett)
                else:
                    valid_words.append(word)
    return valid_words
# result = get_pure_user_words(get_user_words(), generate_grid(),
#  get_words('/Users/sofiyamandryk/Desktop/OP/op2/en.txt', generate_grid()))
# print(result)

def main():
    """
    This is the main function for the game that coordinates the workflow.
    It generates letters, chooses a random word type, and checks the user's words.
    """
    letters = generate_grid()  #random letters
    letters_flat = [letter for row in letters for letter in row]
    print(f"Літери: {letters_flat}")

    user_words = get_user_words()  # nput
    words_from_dict = get_words('/Users/sofiyamandryk/Downloads/base.lst', letters_flat)

    correct_words = get_pure_user_words(user_words, letters_flat, words_from_dict)
    missed_words = [word for word in words_from_dict if word not in user_words]

    print(f"Правильно запропоновані слова: {correct_words}")
    print(f"Пропущені слова: {missed_words}")
