import estimations


def minimax(coordinates, radiuses, values, owner, level, currentLevel = 1):
    '''
    todo: documentation
    '''
    profit, selectNode = None, None
    PLAYER_POINT = 1 if currentLevel % 2 == 0 else 0
    profit = 999999999 if PLAYER_POINT else 0
    visitedNodes = []
    if level <= currentLevel * 2:
        return estimations.typesProfitEstimation(coordinates, radiuses, values)
    for origin in coordinates:
        if not owner[origin]:
            continue
        for point in coordinates:
            if (owner.get(point) is None) and (point not in visitedNodes) and \
                    (estimations.distance(origin, point) <= radiuses[origin]):
                visitedNodes.append(point)
                owner[point] = PLAYER_POINT
                branchProfit = minimax(coordinates, radiuses, values, owner, level, currentLevel + 1)
                if (PLAYER_POINT and branchProfit < profit) or (not PLAYER_POINT 
                        and branchProfit > profit):
                    profit = branchProfit
                    selectNode = point
    return (selectNode, profit)

if __name__ == '__main__':
    a = [(2, 2), (5, 1), (5, 3), (3.1, 3.6), (3, 1)]
    b = {(2, 2): 2, (5, 1): 2, (5, 3): 2, (3.1, 3.6): 2, (3, 1): 2}
    c = {(2, 2): 2, (5, 1): 5, (5, 3): 7, (3.1, 3.6): 8, (3, 1): 13}
    d = {(2, 2): 1}
    # res = estimations.typesProfitEstimation(a, b, c)
    # print('\n' + '#' * 30)
    # for i in res:
    #     print(c[i], i, res[i])
    # print('#' * 30)
    res = minimax(a, b, c, d, 1)
    print(res)

