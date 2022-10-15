'''
Find the sum of the digits of a positive integer number using recursion.
'''

from re import A


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



'''
Calculate the greatest common divisor using recursion
'''

def GCD(numberA, numberB):
    print(numberA, numberB)
    if(numberA%numberB==0):
        return numberB    
    numberA,numberB= numberB,numberA%numberB
    return GCD(numberA,numberB )

