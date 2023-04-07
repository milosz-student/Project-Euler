"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

c = 1000 - a - b

Find the product abc.
a^2 + b^2 = c^2
a^2 + b^2 = (1000 - a - b)^2
a^2 + b^2 = a^2 + 2 a b - 2000 a + b^2 - 2000 b + 1000000
0 = 2 a b - 2000 a - 2000 b + 1000000
0 = ab - 1000a - 1000b + 500000
0 = b(a-1000) -1000a + 500000
-500000+1000a = b(a-1000)
b = (-500000+1000a)/(a-1000)
0<a<1000
but a<b<c
so a<333
O(N/3)
"""
for a in range(1, 1000 // 3):
    b = (-1 * 500000 + 1000 * a) / (a - 1000)
    c = 1000 - a - b
    if not b.is_integer() or b <= 0 or not c.is_integer() or a > b or b > c:
        continue
    b = int(b)
    c = int(c)
    if a**2 + b**2 == c**2:
        print(a, b, c, a * b * c)
        break
