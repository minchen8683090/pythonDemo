"""
合并两个排序的整数数组A和B变成一个新的数组
"""


def merge_arrays(a, b):
    if a is None:
        return b
    if b is None:
        return a

    if len(a) > len(b):
        big, small = a, b
    else:
        big, small = b, a

    i = 0
    while len(small) > 0:
        value = small[0]
        j = len(big)
        if i == j:
            big.append(value)
            small.remove(value)
        elif value <= big[i]:
            big.insert(i, value)
            small.remove(value)
        else:
            i += 1
    return big
