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

def typesProfitEstimation(coordinates, radiuses):
    '''
    (list, dictionary) -> dictionary
    '''
    estimations = {}
    for origin in coordinates:
        for point in coordinates:
            if distance(origin, point) <= radiuses[origin]:
                pass
    pass
