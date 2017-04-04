import numbers
import decimal
def generatePrimeNumbers(number):
    primeNumbers=[]
    digits=[]
    if type(number)==int:
        if number>1:                
            num = set(j for i in range(2, number+1) for j in range(i*2, number+1, i))
            for x in range(2,number+1):
                if x not in num:
                    primeNumbers.append(x)
            return primeNumbers
        else:
            return "the number is not a prime number"
    elif type(number)==str:
        return 'invalid value'
    
    elif type(number)==list:
        return 'invalid values'

print( generatePrimeNumbers(-1))
