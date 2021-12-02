import os

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def solve(s: str) -> int:
    numbers = [int(line) for line in s.splitlines()]
    for n in numbers:
        pass

    lines = s.splitlines()
    for line in lines:
        pass
    return 0


INPUT_SAMPLE = """
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_SAMPLE, 7)),
)
def test(input_sample: str, expected: int) -> None:
    assert solve(input_sample) == expected


def main() -> int:

    with open("input.txt") as f:
        solve(f.read())

    return 0


if __name__ == "__main__":
    main()
