def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5 + 1), 2):
        if n % i == 0:
            return False
    return True


sum = 0
for i in range(2, 2000000):
    if is_prime(i):
        sum += i
print(sum)
