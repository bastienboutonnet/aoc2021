import os

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def solve(s: str) -> int:
    lines = s.splitlines()
    h_poz = 0
    depth = 0
    aim = 0
    for line in lines:
        direction, increments_str = line.split()
        increments: int = int(increments_str)
        if direction == "up":
            aim -= increments
        elif direction == "down":
            aim += increments
        elif direction == "forward":
            h_poz += increments
            depth += aim * increments
    return h_poz * depth


INPUT_SAMPLE = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


@pytest.mark.parametrize(
    ("input_sample", "expected"),
    ((INPUT_SAMPLE, 900),),
)
def test(input_sample: str, expected: int) -> None:
    assert solve(input_sample) == expected


def main() -> int:

    with open("input.txt") as f:
        print(solve(f.read()))

    return 0


if __name__ == "__main__":
    main()
