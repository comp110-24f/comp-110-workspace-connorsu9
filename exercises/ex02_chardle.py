"""EX02 - Chardle - A cute step towards Wordle."""

__author__ = "730772172"


def input_word() -> str:
    """This function prompts the user for a 5 letter word and will give them an error if the word isnt 5 letters"""
    word = input("Enter a 5 letter word: ")  # input from the user
    if len(word) != 5:  # if the word is not 5 characters will return error
        print("Error: Word must contain 5 characters.")
        exit()
    return word


def input_letter() -> str:
    """this function will take a single letter from the user"""
    char = input("Enter a single character: ")  # input from user
    if len(char) != 1:  # if the input is not a single letter will return an error
        print("Error: Character must be a single character")
        exit()
    return char


def contains_char(word, char) -> None:
    """this function searches the word to see how many times the letter the user used appears"""
    apps = 0
    print("Searching for " + char + " in " + word)
    if char == word[0]:  # if statements determine if the letter is at each index
        print(char + " found at index 0")
        apps += 1
    if char == word[1]:
        print(char + " found at index 1")
        apps += 1
    if char == word[2]:
        print(char + " found at index 2")
        apps += 1
    if char == word[3]:
        print(char + " found at index 3")
        apps += 1
    if char == word[4]:
        print(char + " found at index 4")
        apps += 1
    if (
        apps == 0
    ):  # this if statement checks the appearances of the letter in the word and prints it to the screen
        print("No instances of " + char + " found in " + word)
    else:
        print(str(apps) + " instances of " + char + " found in " + word)


def main() -> None:
    """the main function combines all the functions into one area for simple use"""
    contains_char(word=input_word(), char=input_letter())


if __name__ == "__main__":
    main()
