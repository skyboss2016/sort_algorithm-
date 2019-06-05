"""
希尔排序法:
    1.插入类算法.
    2.本质上是进行了分组的排序算法, 分组的方法是间隔一定长度的位置的数字划分为一组进行插入排序
    3.将长度间隔减小, 再次进行插入排序, 最后间隔变为1
    4.使用while循环的从右到左是最快的希尔循环.非常快.

    序列:
    [6, 3, 5, 8]
    分组:
    6, 5,15
    3, 8,
    作插入排序
    5, 6,
    3, 8
    还原成序列
    [5, 3, 6, 8]
    再分组的话还是这个列表,
    作插入排序
    3, 5, 6, 8
"""


# 从右到左内循环使用while 最快.
def shell_sort(unsort):
    n = len(unsort)
    step = n // 2
    while step > 0:
        for i in range(step, n):
            while i - step >= 0 and unsort[i] < unsort[i - step]:
                unsort[i], unsort[i - step] = unsort[i - step], unsort[i]
                i -= step
        step //= 2
    return unsort


def shell_sort1(unsort):
    n = len(unsort)
    step = n // 2
    while step > 0:
        for i in range(step, n):
            num = i % step
            while num < i:
                if unsort[num] > unsort[i]:
                    unsort[num], unsort[i] = unsort[i], unsort[num]
                num += step
        step //= 2


def shell_sort2(unsort):
    n = len(unsort)
    step = n // 2
    while step > 0:
        for i in range(step, n):
            num = i % step
            for j in range(num, i, step):
                if unsort[j] > unsort[i]:
                    unsort[j], unsort[i] = unsort[i], unsort[j]
        step //= 2


# 从右到左内循环使用for, 很慢是while的两倍
def shell_sort3(unsort):
    n = len(unsort)
    step = n // 2
    while step > 0:
        for i in range(step, n):
            for j in range(i, 0, -step):
                if unsort[j - step] > unsort[j]:
                    unsort[j - step], unsort[j] = unsort[j], unsort[j - step]
                else:
                    break
        step //= 2
    return unsort


if __name__ == '__main__':
    from test_sort import test_sort_algorithm

    print('希尔排序法, 从右到左, while')
    test_sort_algorithm(shell_sort)
    print('希尔排序法, 从左到右, while')
    test_sort_algorithm(shell_sort1)
    print('希尔排序法, 从左到右, for')
    test_sort_algorithm(shell_sort2)
    print('希尔排序法, 从右到左, for')
    test_sort_algorithm(shell_sort3)
