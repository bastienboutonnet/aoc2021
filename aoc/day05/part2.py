import os
import timeit
from collections import Counter

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def solve(s: str) -> int:
    lines = s.splitlines()
    vents = Counter()
    for line in lines:
        right, left = line.split("->")
        x1, y1 = [int(i) for i in right.split(",")]
        x2, y2 = [int(i) for i in left.split(",")]
        if x1 == x2:
            for y_increment in range(min(y1, y2), max(y1, y2) + 1):
                vents[(x1, y_increment)] += 1
        elif y1 == y2:
            for x_increment in range(min(x1, x2), max(x1, x2) + 1):
                vents[(x_increment, y1)] += 1
        elif abs(x1 - x2) == abs(y1 - y2):
            diagonal_x = 1 if x1 < x2 else -1
            diagonal_y = 1 if y1 < y2 else -1
            for diag_increment in range(abs(x1 - x2) + 1):
                if (x1, y1) != (x2, y2):
                    vents[(x1 + diag_increment * diagonal_x, y1 + diag_increment * diagonal_y)] += 1

    dangerous_areas = 0
    for _, counts in vents.most_common():
        if counts > 1:
            dangerous_areas += 1
        else:
            pass
    return dangerous_areas


INPUT_SAMPLE = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


@pytest.mark.parametrize(
    ("input_sample", "expected"),
    ((INPUT_SAMPLE, 12),),
)
def test(input_sample: str, expected: int) -> None:
    assert solve(input_sample) == expected


def main() -> int:

    with open("input.txt") as f:
        print(solve(f.read()))

    return 0


if __name__ == "__main__":
    print(timeit.timeit(main, number=1))
