import primeNumber
import happyNumbers

def distance(origin, related):
    '''
    (tuple, tuple) -> number
    Return distance between two points.
    >>> distance((0, 0), (1, 1))
    1.4142135623730951
    >>> distance((0, 0), (0, 0))
    0.0
    >>> distance((1, 1.5),(9.1, 3.3332))
    8.304855341304869
    '''
    return ((origin[0] - related[0]) ** 2 + \
                (origin[1] - related[1]) ** 2) ** 0.5 

def typesProfitEstimation(coordinates, radiuses, values):
    '''
    (list, dictionary, dictionary) -> dictionary
    Return a dictionary of Type estimations for each point 
    by its given coordinates, radiuses and values of the points.
    '''

    def calcEstimation(primes, happies):
        '''
        (integer, integer) -> number
        Return profitability estimation of a given point by 
        its amount of prime and happy neighbors.
        >>> calcEstimation(0, 0)
        0.0
        >>> calcEstimation(10, 2)
        23.323807579381203
        >>> calcEstimation(0, 5)
        5.0
        '''
        return ( (primes + happies) ** 2 + (primes * happies) ** 2) ** 0.5

    estimations = {}
    for origin in coordinates:
        counterPrime = 0
        counterHappy = 0
        for point in coordinates:
            if distance(origin, point) <= radiuses[origin]:
                if primeNumber.primeNumber(values[point]):
                    counterPrime += 1
                if happyNumbers.happyNumbers(values[point]):
                    counterHappy += 1
        estimation = calcEstimation(counterPrime, counterHappy)
        estimations[origin] = estimation
    return estimations

if __name__ == '__main__':
    a = [(2,2),(5,1),(5,3),(1.1, 1.6),(3,1)]
    b = {(2,2) : 2,(5,1) : 2,(5,3) : 2,(1.1, 1.6) : 2,(3,1) : 2}
    c = {(2,2) : 2,(5,1) : 5,(5,3) : 7,(1.1, 1.6) : 8,(3,1) : 13}
    res = typesProfitEstimation(a, b, c)
    print('#' * 10)
    for i in res:
        print(c[i], i, res[i])
