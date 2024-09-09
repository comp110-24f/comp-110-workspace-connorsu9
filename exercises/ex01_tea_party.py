"""The tea party function assignment"""

__author__ = "730772172"


def main_planner(guests: int) -> None:
    """function helps users read the program"""
    # prints a message that summarizes the party
    print("A Cozy Tea Party for " + (str)(guests) + " People!")
    print("Tea Bags: " + (str)(tea_bags(guests)))
    print("Treats: " + (str)(treats(guests)))
    print("Cost: $" + (str)(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """determines the number of teabags needed for the number of people"""
    # calculates the number of teabags needed per person
    return people * 2


def treats(people: int) -> int:
    """returns the number of treats needed for the number of people drinking tea"""
    # calculates the amount of treats based off of the number of teabags
    return (int)(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """Determines the price of tea bags and treats"""
    # calculates the cost of treats and teabags
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    # prompts the user for the number of guests attending
    main_planner(guests=int(input("How many guests are attending your tea party?")))
