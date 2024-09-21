"""EX02 - Chardle - A cute step towards Wordle."""

__author__ = "730772172"


def input_word() -> str:
    """This function prompts the user for a 5 letter word and will give them an error if the word isnt 5 letters"""
    word: str = input("Enter a 5-character word: ")  # input from the user
    if len(word) != 5:  # if the word is not 5 characters will return error
        print("Error: Word must contain 5 characters.")
        exit()
    return word


def input_letter() -> str:
    """this function will take a single letter from the user"""
    letter: str = input("Enter a single character: ")  # input from user
    if len(letter) != 1:  # if the input is not a single letter will return an error
        print("Error: Character must be a single character.")
        exit()
    return letter


def contains_char(word: str, letter: str) -> None:
    """this function searches the word to see how many times the letter the user used appears"""
    count: int = 0
    print("Searching for " + letter + " in " + word)
    if letter == word[0]:  # if statements determine if the letter is at each index
        print(letter + " found at index 0")
        count += 1
    if letter == word[1]:
        print(letter + " found at index 1")
        count += 1
    if letter == word[2]:
        print(letter + " found at index 2")
        count += 1
    if letter == word[3]:
        print(letter + " found at index 3")
        count += 1
    if letter == word[4]:
        print(letter + " found at index 4")
        count += 1

    if count == 0:
        # this if statement checks the appearances of the letter in the word and prints it to the screen
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    """the main function combines all the functions into one area for simple use"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
