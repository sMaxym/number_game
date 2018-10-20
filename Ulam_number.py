def ulamNumbers(number):
    ulam = [1,2]
    coefficient = 0
    for i in range(3,number+1):
        h = (i//2)+1 if i%2==1 else i // 2
        for m in range(1,h):
            if (m in ulam) and (i-m in ulam):
                coefficient += 1
        if coefficient == 1:
            ulam.append(i)
        coefficient = 0
    for k in range(number):
        if number in ulam:
            return True
        else:
            return False 
for num in range(100):
    if ulamNumbers(num):
        print(num, end = ", ")       
