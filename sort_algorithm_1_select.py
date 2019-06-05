"""
选择排序法:
    1.属于选择类排序算法, 同类的算法还有树形选择排序和堆排序,
    2.基本思路就是: 选出最小的数字交换到正确的位置.
    3.外层循环遍历一遍列表, 最后一个就不用了
    4.外层遍历到的位置索引设定为最小值索引,
    5.从这个位置往后一位开始遍历列表, 找到更小的数字的位置更新最小值位置索引.
    6.遍历比较的是当前位置的数字和最小索引数字的大小.
    7.遍历完成后交换最小值索引所在的数字和外层遍历位置的数字
    8.两层循环而且没有提前退出的可能, 时间复杂度为O(n^2)
    9.时间负杂度的计算方法 s + (s-1) + (s-2) + ... + 1 = (s + 1) * (s/2) =  s(s+1)/2 = s^2/2 + s /2
    10.舍去低阶项和常数倍数就是时间复杂度s^2, 这里的s等于n-1, 基于同样的道理就变成了n^2, 记作O(n^2)
"""


# 有一个交换当前外层循环到的位置和内层搜索到的最小值的方案,
# 这个方案交换次数有点多, 还是直接用时间复杂度为O(1)的下标索引吧.
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


# 这是直接交换方案
def select_sort1(unsort):
    n = len(unsort)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if unsort[j] < unsort[i]:
                unsort[j], unsort[i] = unsort[i], unsort[j]
    return unsort


if __name__ == '__main__':
    from test_sort import test_sort_algorithm

    print('下标索引记录')
    test_sort_algorithm(select_sort)
    print('直接交换')
    test_sort_algorithm(select_sort1)
