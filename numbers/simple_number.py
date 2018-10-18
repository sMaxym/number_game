def prime_number(number):
    if (number < 2):
        return False
    for factor  in range(2,number):
        if (number % factor) == 0:
            return False
    return True 
for num in range(100):
    if prime_number(num):
        print(num, end = ", ")