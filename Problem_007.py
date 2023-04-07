"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5 + 1), 2):
        if n % i == 0:
            return False
    return True


prime_numbers = []
i = 2
while True:
    if is_prime(i):
        prime_numbers.append(i)
    if len(prime_numbers) == 10001:
        break
    i += 1

print(prime_numbers[-1])
