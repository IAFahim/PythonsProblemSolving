a = [[1, 2], [1, 3], [10, 40]]


def find_gcd(a, b):
    if (a < b): a, b = b, a
    while (b != 0):
        c = a
        a = b
        b = c % b
    gcd = a
    return gcd


def convertFracts(lst):
    if (len(lst) >= 2):
        D = lst[0][1] * lst[1][1] / find_gcd(lst[0][1], lst[1][1])
        for i in range(2, len(lst)):
            D = D * lst[i][1] / find_gcd(D, lst[i][1])
        D = int(D)
        new_lst = []
        for i in range(len(lst)):
            temp_lst = [lst[i][0] * int(D / lst[i][1]), D]
            new_lst.append(temp_lst)
        return new_lst
    else:
        return lst


print(convertFracts(a))