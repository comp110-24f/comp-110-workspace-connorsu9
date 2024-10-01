"""coordinates file"""

__author__ = "730772172"


def get_coords(xs: str, ys: str) -> None:
    """print formatted pairs of each character in two input strings"""
    idx1: int = 0
    # index variable
    while idx1 < len(xs):
        # nested while loop prints each individual character
        idx2: int = 0
        while idx2 < len(ys):
            print("(" + xs[idx1] + "," + ys[idx2] + ")")
            idx2 += 1
        idx1 += 1


if __name__ == "__main__":
    """puts the whole file together and prevents printing from import"""
    xs = "12"
    ys = "34"
    get_coords(xs, ys)
