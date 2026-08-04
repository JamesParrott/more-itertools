import math
from itertools import repeat, chain, cycle, islice
from typing import Sequence, Iterator

def zip_lcm[T](
    seq0: Sequence[T],
    seq1: Sequence[T],
    *seqs: Sequence[T],
) -> Iterator[tuple[T, ...]]:
    lcm = math.lcm(*map(len, (seq0, seq1, *seqs)))
    repeated_seq0 = repeat(seq0, lcm // len(seq0))
    yield from zip(
        chain.from_iterable(repeated_seq0),
        cycle(seq1),
        *map(cycle, seqs),
    )


def test(func_to_test=zip_lcm):
    def helper(*seqs: str) -> str:
        return " ".join(map("".join, func_to_test(*seqs)))

    assert helper("01", "abc") == "0a 1b 0c 1a 0b 1c"
    assert (
        helper("01", "abcd", "xyz") == "0ax 1by 0cz 1dx 0ay 1bz 0cx 1dy 0az 1bx 0cy 1dz"
    )

    print("all tests pass")

def alternative(*seqs):
    lcm: int = math.lcm(*map(len, seqs))
    yield from islice(zip(*map(cycle,seqs)), lcm)


if __name__ == '__main__':
    test()
    test(alternative)
