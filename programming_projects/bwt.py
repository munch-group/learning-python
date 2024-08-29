"""
Code for working with the Burrows-Wheeler transform and
the FM-index.
"""
from typing import (
    Optional as Opt,
    Iterable as Iter,
    Dict, List
)
from collections import (
    Counter
)

Buckets = Dict[str, int]
Ranks = Dict[str, List[int]]


def suffix_array(x: str) -> List[int]:
    """
    Build a suffix array from the string x.

    The string must be terminated by a sentinel
    character (traditionally we use '$').

    The algorithm runs in O(n² log n) so it is
    inefficient, but smarter algorithms exist.
    """
    sufs = [x[i:] for i, _ in enumerate(x)]
    sufs.sort()
    return [len(x) - len(suf) for suf in sufs]


def print_rotations(x: str, sufs: Opt[Iter[int]] = None) -> None:
    """Print rotations of x.

    The sufs list should be indices into x,
    representing different rotations, or None
    for the usual order.
    """
    sufs = sufs if sufs is not None else range(len(x))
    for i in sufs:
        print(x[i:] + x[:i])


def bwt(x: str, sa: List[int]) -> str:
    """Compute the Burrows-Wheeler transform."""
    return ''.join(x[i-1] for i in sa)


def compute_buckets(x: str) -> Buckets:
    """
    Compute the accumulated sum of the letters in x.

    This is a simple Python version, that is less
    efficient than it could be, but it is fast
    enough for a toy example.
    """
    counts = Counter(x)
    bucks = {a: counts[a] for a in sorted(counts)}
    acc = 0
    for a in bucks:
        bucks[a], acc = acc, acc + bucks[a]
    return bucks


def compute_ranks(x: str) -> Ranks:
    """Compute the ranks of each letter in x."""
    ranks = {a: [0] for a in set(x)}
    for a in ranks:
        for b in x:
            ranks[a].append(ranks[a][-1] + (a == b))
    return ranks


def rotate(i: int, a: str, buckets: Buckets, ranks: Ranks) -> int:
    """
    Rotate index i by putting a in front of it.

    This function does the rotation used for reversing
    the BWT or for searching with the FM-index.
    """
    return buckets[a] + ranks[a][i]


def reverse_bwt(bwt: str) -> str:
    """Reverses a BW-transformed string."""
    buckets = compute_buckets(bwt)
    ranks = compute_ranks(bwt)

    x = ['$'] * len(bwt)
    i = 0
    for j in range(1, len(bwt)):
        x[j] = bwt[i]
        i = rotate(i, bwt[i], buckets, ranks)

    return ''.join(x[::-1])


def fm_index(p: str, x: str, sa: List[int]) -> Iter[int]:
    """
    Find all occurrences of p in x using the FM-index.

    Normally, the preprocessing (building the bwt(x) and the
    two tables) would not be part of each individual search,
    but done once, so we can search efficiently for any number
    of patterns later. This is just a toy example.
    """
    bwt_x = bwt(x, sa)
    buckets = compute_buckets(bwt_x)
    ranks = compute_ranks(bwt_x)

    left, right = 0, len(x)
    for a in reversed(p):
        left = rotate(left, a, buckets, ranks)
        right = rotate(right, a, buckets, ranks)
    yield from sa[left:right]


def get_index(p, x, bwt_x, buckets, ranks):
    left, right = 0, len(x)
    for a in reversed(p):
        left = rotate(left, a, buckets, ranks)
        right = rotate(right, a, buckets, ranks)
    yield from sa[left:right]


x = 'mississippi$'
sa = suffix_array(x)
bwt_x = bwt(x, sa)
buckets = compute_buckets(bwt_x)
ranks = compute_ranks(bwt_x)

p = "ssi"
for i in get_index(p, x, sa, buckets, ranks):
    print(f"{p} matches at x[{i}:] = {x[i:]}")


# sa = suffix_array(x)
# print("asdf", sa)
# print_rotations(x, sa)
# print()

# bwt_x = bwt(x, sa)
# print(f"bwt({x}) = {bwt_x}")

# print(compute_buckets(bwt_x))
# print(compute_ranks(bwt_x))
# print()

# print(reverse_bwt(bwt_x))
# print()

# p = "ssi"
# for i in fm_index(p, x, sa):
#     print(f"{p} matches at x[{i}:] = {x[i:]}")
