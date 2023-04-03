'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

def is_prime(n):
    if n < 2:
        return False
    for i in range(3, int(n ** 0.5 // 2 + 1), 2):
        if n % i == 0:
            return False
    return True


big_number = 600851475143
max = 1
for x in range(2, int(big_number ** 0.5 // 2 + 1)):
    if big_number % x == 0 and is_prime(x):
        max = x
print(max)