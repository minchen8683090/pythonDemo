"""
设计一个算法，计算出n阶乘中尾部零的个数
"""
def calculate_factorial_tail_zero(num):
    count = 0
    temp = int(num / 5)
    while temp != 0:
        count += temp
        temp = int(temp / 5)
    print(count)
