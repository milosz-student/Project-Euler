'''
The sum of the squares of the first ten natural numbers is,
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
n = 100
#1/3n^2 + 1/2n^2 + 1/6n
sum_squares = 1/3*n^2 + 1/2*n^2 + 1/6*n
square_sum = ((1+n)*n//2)**2
print(square_sum-sum_squares)