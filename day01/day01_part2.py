import os

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def solve(s: str) -> int:
    numbers = [int(line) for line in s.splitlines()]
    count = 0
    for i in range(3, len(numbers)):
        if sum(numbers[i - 2 : i + 1]) > sum(numbers[i - 3 : i]):
            count += 1

    return count


INPUT_SAMPLE = """\
199
200
208
210
200
207
240
269
260
263
"""


@pytest.mark.parametrize(
    ("input_sample", "expected"),
    ((INPUT_SAMPLE, 5),),
)
def test(input_sample: str, expected: int) -> None:
    assert solve(input_sample) == expected


def main() -> int:

    with open("input.txt") as f:
        print(solve(f.read()))

    return 0


if __name__ == "__main__":
    main()
