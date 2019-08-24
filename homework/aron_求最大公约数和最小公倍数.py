def greatest_common_divisor(a, b):
    """
    求两个数的最大公约数(辗转相除法)
    :param a: 数字a
    :param b: 数字b
    """
    _result = a % b
    if _result == 0:
        return b
    return greatest_common_divisor(b, _result)


def least_common_multiple(a, b):
    """
    求两个数的最小公倍数
    :param a: 数字a
    :param b: 数字b
    """
    return (a * b) // greatest_common_divisor(a, b)


if __name__ == "__main__":
    result = greatest_common_divisor(319, 377)
    print(result)
