game_points = [94, 104, 87]


def display(int_lists: list[int]) -> None:
    """displays all elements in list"""
    idx = 0

    while idx < len(int_lists):
        print(int_lists[idx])
        idx += 1


display(int_lists=game_points)
