def happy_numbers(number):
    if number < 0:
        return False
    if (number == 1) or (number == 7):
        return True
    while number:
        sum_of_squares = 0 
        digits = []
        st_num = str(number)
        for i in range(len(st_num)):
            digit = number % 10
            number //= 10
            digits.append(digit)
        for m in range(len(digits)):
            sum_of_squares += digits[m]**2
        if sum_of_squares == 1:
            return True
        elif  2 <= sum_of_squares <= 9:
            return False 
        elif sum_of_squares >= 10:
            number = sum_of_squares
        