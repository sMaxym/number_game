import primeNumber
import happyNumbers
import ulamNumber


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
    return ((origin[0] - related[0]) ** 2 + (origin[1] -
            related[1]) ** 2) ** 0.5


def typesProfitEstimation(coordinates, radiuses, values):
    '''
    (list, dictionary, dictionary) -> dictionary
    Return a dictionary of Type estimations for each point
    by its given coordinates, radiuses and values of the points.
    '''

    def calcEstimation(primes, happies, ulam):
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
        return ((primes + happies + ulam) ** 2 + (primes * \
                    happies * ulam) ** 2) ** 0.5

    estimations = {}
    for origin in coordinates:
        counterPrime = 0
        counterHappy = 0
        counterUlam = 0
        for point in coordinates:
            if distance(origin, point) <= radiuses[origin]:
                if primeNumber.primeNumber(values[point]):
                    counterPrime += 1
                if happyNumbers.happyNumbers(values[point]):
                    counterHappy += 1
                if ulamNumber.ulamNumbers(values[point]):
                    counterUlam += 1
        estimation = calcEstimation(counterPrime, counterHappy, counterUlam)
        estimations[origin] = estimation
    return estimations
