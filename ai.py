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

def updateProfit(profit, diff, turn, playerIndex = 0, aiIndex = 1):
    '''
    (number, number, intger) -> number
    Return updated value of a profit based on the current turn.
    >>> updateProfit(1, 0.5, 1)
    1.5
    >>> updateProfit(-5.1, 0.1, 0)
    -5.2
    '''
    if turn == playerIndex:
        profit -= diff
    elif turn == aiIndex:
        profit += diff
    return round(profit, 10)

def selectProper(data, turn, playerIndex = 0, aiIndex = 1):
    '''
    (list, number) -> number
    Return max element from "data" array if turn 
    is player indexed, otherwise return min element.
    '''
    proper = None
    if turn == playerIndex:
        proper = min(data)
    elif turn == aiIndex:
        proper = max(data)
    return proper
import doctest
def listSubtraction(list, sublist):
    '''
    (list, list) -> list
    Return subtraction of of list and sublist.
    >>> listSubtraction([1, 1, 5], [1])
    [5]
    '''
    res = []
    for item in list:
        toAdd = True
        for subitem in sublist:
            if item == subitem:
                toAdd = False
        if toAdd:
            res.append(item)
    return res
doctest.testmod()
def minimax(coordinates, radiuses, values, owner, level, currentLevel = 1, playerIndex = 0, aiIndex = 1):
    '''
    todo: documentation
    '''
    AI = aiIndex
    PLAYER = playerIndex
    TURN = PLAYER if currentLevel % 2 == 0 else AI
    nodeCandidates = []
    distanceSkip = 0
    isFinal = True

    if currentLevel >= level * 2:
        enemyCoords = associatedElements(owner, TURN, coordinates)
        estimationCoords = listSubtraction(coordinates, enemyCoords)
        estimated = estimations.typesProfitEstimation(estimationCoords, radiuses, values)
        return estimated
        
    for node in coordinates:
        ownerPoints = associatedElements(owner, TURN, coordinates)
        if hasAssociation(owner, node):
            continue
        if not distanceAvailability(node, radiuses[node], ownerPoints):
            distanceSkip += 1
            continue
        isFinal = False
        profit = 0
        currentOwner = owner.copy()
        currentOwner[node] = TURN
        localProfit = minimax(coordinates, radiuses, values, currentOwner, level, currentLevel + 1)
        if isinstance(localProfit, dict):
            localProfit = localProfit[node]
        profit = updateProfit(profit, localProfit, TURN)
        nodeCandidates.append(profit)
    if distanceSkip:
        #TODO: redo with DRY
        profit = 0
        localProfit = minimax(coordinates, radiuses, values, owner, level, currentLevel + 1)
        if isinstance(localProfit, dict):
            localProfit = localProfit[node]
        profit = updateProfit(profit, localProfit, TURN)
        nodeCandidates.append(profit)
        properProfit = selectProper(nodeCandidates, TURN)  
        return localProfit
    elif isFinal:
        enemyCoords = associatedElements(owner, TURN, coordinates)
        estimationCoords = listSubtraction(coordinates, enemyCoords)
        estimated = estimations.typesProfitEstimation(estimationCoords, radiuses, values)
        return estimated

    properProfit = selectProper(nodeCandidates, TURN)    
    return properProfit

    # TODO: Check if there any non owned nodes
    # if isFinal:
    #     estimated = estimations.typesProfitEstimation(coordinates, radiuses, values)
    #     return estimated

if __name__ == '__main__':
    a = [(2, 2), (5, 1), (5, 3), (3.1, 3.6), (3, 1)]
    b = {(2, 2): 2, (5, 1): 2, (5, 3): 2, (3.1, 3.6): 2, (3, 1): 2}
    c = {(2, 2): 2, (5, 1): 5, (5, 3): 7, (3.1, 3.6): 8, (3, 1): 13}
    d = {(2, 2): 0, (5, 1): 1}
    # res = estimations.typesProfitEstimation(a, b, c)
    # print('\n' + '#' * 30)
    # for i in res:
    #     print(c[i], i, res[i])
    # print('#' * 30)
    
    res = minimax(a, b, c, d, 4)
    print(res)
    # # print(associatedElements({(1,1): 2, (0, 0): 3, (10, 5): -1, (1, -1): 2}, 2, [(1,1), (2,3), (3,3), (0, 0)]))

