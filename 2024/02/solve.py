import collections.abc as cabc
import typing
import itertools as it


def parse(input_file):

    with open(input_file) as f:
        for line in f.readlines():
            yield [*map(int, line.split())]


def safe(seq: cabc.Iterable[int]):
    diffs = [j - i for i, j in it.pairwise(seq)]
    return len({d > 0 for d in diffs}) == 1 and all(1 <= abs(d) <= 3 for d in diffs)


def lax(seq: list[int]):
    return any(safe([*seq[:i], *seq[i + 1 :]]) for i in range(len(seq)))


def part1():
    return sum(map(safe, parse('sample.txt')))


def part2():
    return sum(map(lax, parse('input.txt')))

print(part1())
print(part2())
