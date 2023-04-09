'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
2^10 = 1024 sum 7
2^9 = 512 sum 8
2^8 = 256 sum 13
2^7 = 128 sum 11
2^6 = 64 sum 10
2^5 = 32 sum 5
2^4 = 16 sum 7
2^3 = 8 sum 8
What is the sum of the digits of the number 2^1000?

2^1000 = 2^(10^3)
'''
exponent = 1000
number = [2] # store number in the array
for i in range(1,exponent):
    carry_flag = False
    for j in range(len(number)):
        tmp = number[j]*2
        if carry_flag:
            tmp+=1
            carry_flag = False
        if tmp > 9:
            tmp = tmp%10
            if j < len(number) - 1:
                carry_flag = True
            elif j == len(number) - 1:
                number.append(1)
        number[j] = tmp

number.reverse()
print(number)
print(sum(number))



