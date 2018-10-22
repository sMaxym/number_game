import estimations

def distanceAvailability(origin, radius, points):
    '''
    (tuple, list, dictionary) -> boolean
    Return True if origin is in range of at least 
    one point of points list, otherwise False.
    '''
    for point in points:
        if radius >= estimations.distance(origin, point):
            return True
        else: 
            return False

def associatedElements(associations, interface, elements):
    '''
    (dictionary, number, list) -> list
    Return list of associated elements from a list "elements", 
    where each element associated with a number "interface".
    >>> associatedElements({(1,1): 2, (0, 0): 3, (10, 5): -1, (1, -1): 2}, 2, [(1,1), (2,3), (3,3), (0, 0)])
    [(1, 1)]
    '''
    associatedElm = []
    for element in elements:
        if associations.get(element) == interface:
            associatedElm.append(element)
    return associatedElm

def hasAssociation(associations, element):
    '''
    (dictionary, tuple) -> boolean
    Return if dictionary "associations" has the key "element".
    >>> hasAssociation({1: 2}, 1)
    True
    >>> hasAssociation({(1, 1): 1}, 2)
    False
    '''
    if associations.get(element) is None:
        return False
    else:
        return True

def minimax(coordinates, radiuses, values, owner, level, currentLevel = 1, playerIndex = 0, aiIndex = 1):
    '''
    todo: documentation
    '''
    AI = aiIndex
    PLAYER = playerIndex
    TURN = PLAYER if currentLevel % 2 == 0 else AI
    currentOwner = owner.clone()
    for node in coordinates:
        ownerPoints = associatedElements(currentOwner, TURN, coordinates)
        if hasAssociation(currentOwner, node) or \
                not distanceAvailability(node, radiuses[node], ownerPoints):
            continue
        
    pass

if __name__ == '__main__':
    a = [(2, 2), (5, 1), (5, 3), (3.1, 3.6), (3, 1)]
    b = {(2, 2): 2, (5, 1): 2, (5, 3): 2, (3.1, 3.6): 2, (3, 1): 2}
    c = {(2, 2): 2, (5, 1): 5, (5, 3): 7, (3.1, 3.6): 8, (3, 1): 13}
    d = {(2, 2): 0}
    # res = estimations.typesProfitEstimation(a, b, c)
    # print('\n' + '#' * 30)
    # for i in res:
    #     print(c[i], i, res[i])
    # print('#' * 30)
    
    # res = minimax(a, b, c, d, 2)
    # print(res)
    # print(associatedElements({(1,1): 2, (0, 0): 3, (10, 5): -1, (1, -1): 2}, 2, [(1,1), (2,3), (3,3), (0, 0)]))

