'''
Find the sum of the digits of a positive integer number using recursion.
'''

def sumOfDigit(digit):
    
    if digit ==0:
        return 0
    return digit%10 + sumOfDigit(digit//10)

# print(sumOfDigit(349))

'''
Calculate the Power of a number using recursion

'''

def powerOfANumber(number,exponent):
    if exponent==0:
        return 1
    return number* powerOfANumber(number, exponent-1)
print(powerOfANumber(5,4))