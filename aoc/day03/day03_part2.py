import os
import timeit
from collections import Counter

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def solve(s: str) -> int:
    lines = s.splitlines()
    oxygen = lines
    carbon = lines
    i = 0
    while len(oxygen) > 1 or len(carbon) > 1:
        most_common = 0
        oxy_bit = [row[i] for row in oxygen]
        most_common = Counter(oxy_bit).most_common()
        if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
            most_common = max(most_common[0][0], most_common[1][0])
        else:
            most_common = most_common[0][0]
        least_commons = 0
        carbon_bits = [row[i] for row in carbon]
        least_commons = Counter(carbon_bits).most_common()
        if len(least_commons) > 1 and least_commons[0][1] == least_commons[1][1]:
            least_commons = min(least_commons[0][0], least_commons[1][0])
        else:
            least_commons = least_commons[-1][0]
        oxygen = [row for row in oxygen if row[i] == most_common]
        carbon = [row for row in carbon if row[i] == least_commons]
        i += 1
    return int(oxygen[0], 2) * int(carbon[0], 2)


INPUT_SAMPLE = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


@pytest.mark.parametrize(
    ("input_sample", "expected"),
    ((INPUT_SAMPLE, 230),),
)
def test(input_sample: str, expected: int) -> None:
    assert solve(input_sample) == expected


def main():

    with open("input.txt") as f:
        print(solve(f.read()))


if __name__ == "__main__":
    print(timeit.timeit(main, number=1))
