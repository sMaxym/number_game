def happy_numbers(number):
    if number < 0:
        return False
    if (number == 1) or (number == 7):
        return False
    for i in range(number):
        
