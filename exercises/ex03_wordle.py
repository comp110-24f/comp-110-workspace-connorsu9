"""EX04 Wordle creating a wordle game in python"""

__author__ = "730772172"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def input_guess(sw_length: int = 5) -> str:
    """keeps prompting user for 5 letter word"""
    # prompts user for input
    guess = input(f"Enter a {sw_length} character word: ")
    # while loop checks whether the users answer is the desired length
    while len(guess) != sw_length:
        guess = input(f"That wasn't {sw_length} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char: str) -> bool:
    """Searches a string for a specific character at each index, return true if found"""
    # asserting an assumption that char will always be one character
    assert len(char) == 1
    idx: int = 0
    # loop through each character in a string to see if it matches char
    while idx < len(secret_word):
        if secret_word[idx] == char:
            return True
        idx += 1
    return False


def emojified(guess: str, secret_word: str) -> str:
    """returns emojis of correct letter position, correct letters,
    and incorrect letters"""
    assert len(guess) == len(secret_word)
    word_string: str = ""
    idx1: int = 0
    # while loop checks the position of each character and compares the words
    while idx1 < len(secret_word):
        # if statement checks whether the box should be green, yellow, or white
        if secret_word[idx1] == guess[idx1]:
            word_string += GREEN_BOX
        elif contains_char(secret_word, guess[idx1]):
            word_string += YELLOW_BOX
        else:
            word_string += WHITE_BOX
        idx1 += 1
    return word_string


def main(secret_word: str) -> None:
    """the entrypoint of the program and main game loop."""
    idx = 1
    # while loop starts at 1 and goes up to 6
    while idx < 7:
        print(f"=== Turn {idx}/6 ===")
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            print(f"You won in {idx}/6 turns!")
            exit()
        idx += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main("codes")
