# Utility functions written by bildad

# Factorial

def factorial(number):
    """
    This function calculates the factorial of a number.
    Time complexity O(n)
    Space complexity O(1)
    :param number: int
    :return: number!
    """

    if number < 0:
        return "not defined at the moment"

    factorial = 1
    for i in range(1, number+1):
        factorial = factorial * i

    return factorial

# print(factorial(8))


def list_combinations(n,r):
    from itertools import combinations

    comb = combinations(n,r)

    return list(comb)

# [print(sum(x)) for x in list_combinations([1,3,5,7,9,11,13,15], 3) ]

