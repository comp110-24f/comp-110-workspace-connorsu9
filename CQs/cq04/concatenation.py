"""add two strings together"""

__author__ = "730772172"


def concat(string1: str, string2: str) -> str:
    """combines two input strings"""
    # add two strings
    return string1 + string2


if __name__ == "__main__":
    """puts the whole file together and prevents printing from import"""
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))
