def primeNumber(number):
    '''
    int -> boolean
    Сheck if number is prime or not
    >>> primeNumbers(11)
    True
    >>> primeNumbers(-8)
    False
    >>> primeNumbers(96)
    False
    '''
    if (number < 2):
        return False
    for factor  in range(2,number):
        if (number % factor) == 0:
            return False
    return True
if __name__ == "__main__":
    # Loop for generation prime numbers  
        for num in range(100):     
            if primeNumber(num):
                print(num, end = ", ")
