"Functions Challenge Question"

__author__ = "730772172"


def mimic(message: str) -> str:
    """mimic a string back to the user"""
    return message


def main() -> None:
    """the main pulls the function together"""
    print(mimic(message=input("What is your message? ")))


if __name__ == "__main__":
    main()
