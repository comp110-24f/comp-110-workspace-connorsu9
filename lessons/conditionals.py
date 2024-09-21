"""practice with conditionals"""


def less_than_10(num: int) -> bool:
    """return true if num is less than 10"""
    dub: int = num * 2
    print(dub)
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


def get_weather_report() -> str:
    """gets the weather"""
    weather = input("What is the weather? ")

    if (weather == "rainy") or (weather == "cold"):
        print("bring a jacket!")
    elif weather == "hot":
        print("keep cool out there")
    else:
        print("I don't recognize this weather")

    return weather


get_weather_report()
