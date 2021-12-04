import os
import timeit

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def is_won(board):
    # eval row
    for row in board:
        print(row)
        row_won = not any(row)
        if row_won:
            return True
        # column
    col = 0
    col_n = len(row)
    while col < col_n:
        column = [x[col] for x in board]
        if not any(column):
            return True
        col += 1


def solve(s: str) -> int:
    lines = s.splitlines()
    draws = lines[0].split(",")
    boards = [[x.split() for x in i.split("\n")] for i in "\n".join(lines[2:]).split("\n\n")]
    boards = [[list(map(int, lst)) for lst in x] for x in boards]
    for draw in draws:
        for board_ix, board in enumerate(boards):
            print(board)
            for board_row_i, row in enumerate(board):
                for i, number in enumerate(row):
                    if number == int(draw):
                        boards[board_ix][board_row_i][i] = None
            # eval row
            if is_won(board):
                print(board)
                return sum(filter(None, sum(filter(None, board), []))) * int(draw)
    return 0


INPUT_SAMPLE = """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


@pytest.mark.parametrize(
    ("input_sample", "expected"),
    ((INPUT_SAMPLE, 4512),),
)
def test(input_sample: str, expected: int) -> None:
    assert solve(input_sample) == expected


def main() -> int:

    with open("input.txt") as f:
        print(solve(f.read()))

    return 0


if __name__ == "__main__":
    print(timeit.timeit(main, number=1))
