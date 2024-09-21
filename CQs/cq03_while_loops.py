__author__ = "730772172"


def num_instances(phrase: str, search_char: str) -> int:
    """this function will count the amount of times search_char appears in a string"""
    count = 0
    index = 0
    # count keeps track of the instances of the character
    # and index keeps track of the position
    while index < len(phrase):
        if phrase[index] == search_char:
            # if the character in the string at the index
            # is the same as the character it increases count by 1
            count += 1
        index += 1
    return count


# calling the function
print(num_instances("alphabet", "a"))
