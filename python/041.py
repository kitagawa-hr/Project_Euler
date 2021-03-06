"""
Project Euler Problem 41
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

import itertools

from functions import list_to_num, is_prime


def main():
    for m in range(1, 10)[::-1]:
        perms = [list_to_num(x) for x in
                 itertools.permutations(range(1, m + 1), m)]
        for num in perms[::-1]:
            if is_prime(num):
                print(num)
                return


if __name__ == '__main__':
    main()
