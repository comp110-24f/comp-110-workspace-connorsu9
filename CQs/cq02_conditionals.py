"""Challenge question 2!"""

__author__ = "730772172"


def guess_a_number() -> None:
    """function asks user to guess a number and tells them if they are correct or not"""
    secret: int = 7
    # prompt user for a number
    x = input("Guess a number: ")
    print("Your guess was " + str(x))
    # if statement lets user know if the numbers are correct or too high or too low
    if int(x) == secret:
        print("You got it!")
    elif int(x) > secret:
        print("Your guess was too high! The secret number is " + str(secret))
    elif int(x) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
