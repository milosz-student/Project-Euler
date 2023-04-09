'''
Starting in the top left corner of a 2×2 grid, 
and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
'''
def factorial(n):
    if n>1:
        return n*factorial(n-1)
    return 1


size = 20

possibilites = factorial(size*2)/(factorial(size)*factorial(size))
print(possibilites)