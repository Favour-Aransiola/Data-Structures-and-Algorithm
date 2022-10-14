'''
Find the sum of the digits of a positive integer number using recursion.
'''

def sumOfDigit(digit):
    
    if digit ==0:
        return 0
    return digit%10 + sumOfDigit(digit//10)

print(sumOfDigit(349))