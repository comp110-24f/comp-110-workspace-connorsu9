"""practice with conditionals"""


def less_than_10(num: int) -> bool:
    """return true if num is less than 10"""
    if num < 10:
        return True
    return False


print(less_than_10(12))


def check_first_letter(word: str, letter: str) -> str:
    """returns if they match"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter("happy", "h"))
