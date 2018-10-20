def ulamNumbers(number):
    '''
    int -> boolen
    Function check if number is Ulam or not
    >>> ulamNumber(6)
    True
    >>> ulamNumber(29)
    False
    >>> ulamNumber(-9)
    False
    '''
    if number <= 0:
        return False
    ulam = [1,2]
    coefficient = 0
    for helpForUlam1 in range(3,number+1):
        indicator = (helpForUlam1//2)+1 if helpForUlam1%2==1\
                                       else helpForUlam1 // 2
        for helpForUlam2  in range(1,indicator):
            if (helpForUlam2 in ulam) and \
            (helpForUlam1-helpForUlam2 in ulam):
                coefficient += 1
        if coefficient == 1:
            ulam.append(helpForUlam1)
        coefficient = 0
    for overtaking in range(number):
        if number in ulam:
            return True
        else:
            return False
if __name__ == "__main__":
    # Loop for generation Ulam numbers         
    for num in range(100):
        if ulamNumbers(num):
            print(num, end = ", ")       
