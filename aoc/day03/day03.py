import os

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def solve(s: str) -> int:
    lines = s.splitlines()
    gamma_bits = [0] * len(lines[0])
    for line in lines:
        for i, v in enumerate(line):
            if int(v) == 1:
                gamma_bits[i] += 1
    print(gamma_bits)
    gamma_value = [0] * len(lines[0])
    epsilon_value = [0] * len(lines[0])
    for i in range(len(gamma_bits)):
        if gamma_bits[i] > len(lines) // 2:
            gamma_value[i] += 1
        else:
            epsilon_value[i] += 1
    gamma_value = [str(i) for i in gamma_value]
    gamma_value = "".join(gamma_value)
    epsilon_value = [str(i) for i in epsilon_value]
    epsilon_value = "".join(epsilon_value)
    return int(gamma_value, 2) * int(epsilon_value, 2)


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


def main() -> int:

    with open("input.txt") as f:
        print(solve(f.read()))

    return 0


if __name__ == "__main__":
    main()
