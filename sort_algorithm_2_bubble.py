"""
冒泡排序法:
    1.相邻位置的数字进行交换, 例如[3, 2, 1]交换顺序为3<->2([2, 3, 1]), 3<->1([2, 1, 3])
    2.可以记录交换次序, 当一次从前往后的遍历没有发生交换就可以退出了.
    3.先确定循环次数, 这是外层循环要做的事,
    4.内层循环就是逐个交换, 吧较大的数字往后换.
    5.由此可见, 冒泡排序法的最坏时间复杂度为O(n^2)
    6.将大数往后换和将小数往前换本质上没区别.
"""


def bubble_sort(unsort):
    n = len(unsort)
    # 控制循环次数
    for i in range(1, n):
        count = 0
        # 控制交换次数
        for j in range(n - i):
            if unsort[j] > unsort[j + 1]:
                unsort[j], unsort[j + 1] = unsort[j + 1], unsort[j]
                count += 1
        if count == 0:
            break
    return unsort


if __name__ == '__main__':
    from test_sort import test_sort_algorithm

    test_sort_algorithm(bubble_sort)
