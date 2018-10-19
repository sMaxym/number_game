def happyNumbers(number):
    if number < 0:
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
        
for num in range(1000000):
    if happyNumbers(num):
        print(num, end = ", ")
