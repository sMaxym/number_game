import estimations


if __name__ == '__main__':
    a = [(2, 2), (5, 1), (5, 3), (1.1, 1.6), (3, 1)]
    b = {(2, 2): 2, (5, 1): 2, (5, 3): 2, (1.1, 1.6): 2, (3, 1): 2}
    c = {(2, 2): 2, (5, 1): 5, (5, 3): 7, (1.1, 1.6): 8, (3, 1): 13}
    res = estimations.typesProfitEstimation(a, b, c)
    print('\n' + '#' * 30)
    for i in res:
        print(c[i], i, res[i])
    print('#' * 30)
