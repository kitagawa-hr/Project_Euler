"""
Project Euler Problem 50
========================

The prime 41, can be written as the sum of six consecutive primes:

                       41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

from functions import is_prime, gen_num

N = 1000000


def main():
    primes = (x for x in gen_num(lim=N) if is_prime(x))
    cumsum = [0]
    ret = 0
    for prime in primes:
        ret += prime
        cumsum.append(ret)
    # cumsum = [0, 2, 5, 10, ...]
    # Sum[l..r] = cumsum[r] - cumsum[l]
    max_length = 1
    ans = None
    for left, c in enumerate(cumsum):
        right = left + max_length
        while(right < len(cumsum)):
            s = cumsum[right] - cumsum[left]
            if(s > N):
                break
            if is_prime(s):
                max_length = right - left
                ans = s
            right += 1
    print(ans)
if __name__ == '__main__':
    main()