def happyNumbers(number):
    '''
    int -> boolean
    Сheck if number is happy or not
    >>> happyNumbers(7)
    True
    >>> happyNumbers(-8)
    False
    >>> happyNumbers(96)
    False
    '''
    if number <= 0:
        return False
    if (number == 1) or (number == 7):
        return True
    while number:
        sumOfSquares = 0 
        digits = []
        stNum = str(number)
        for i in range(len(stNum)):
            digit = number % 10
            number //= 10
            digits.append(digit)
        for m in range(len(digits)):
            sumOfSquares += digits[m]**2
        if sumOfSquares == 1:
            return True
        elif  2 <= sumOfSquares <= 9:
            return False 
        elif sumOfSquares >= 10:
            number = sumOfSquares
# Loop for generation happy numbers                    
for num in range(100):
    if happyNumbers(num):
        print(num, end = ", ")