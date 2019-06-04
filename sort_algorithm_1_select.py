"""
选择排序法:
    1.最基本的排序算法, 都称不上是算法吧.
    2.基本思路就是选择最大或最小数字和正确的位置的数字进行交换(以最小举例)
    3.确定循环次数, 当然有多长就循环多少次, 这是外层循环的事
    4.内层循环主要是选出最小的那个数字在哪儿.
    5.交换把最小的数字换到前面去.
    6.两层循环而且没有提前退出的可能, 时间复杂度为O(n^2)
"""


def select_sort(unsort):
    n = len(unsort)
    # 控制循环次数
    for i in range(n - 1):
        min_index = i
        # 找到最小值
        for j in range(i + 1, n):
            if unsort[j] < unsort[min_index]:
                min_index = j
        if min_index != i:
            unsort[min_index], unsort[i] = unsort[i], unsort[min_index]
    return unsort


if __name__ == '__main__':
    from test_sort import test_sort_algorithm

    test_sort_algorithm(select_sort)
