"""
插入排序法:
    1.基本思路就像是整理扑克牌, 从左往右把牌依次插到左边合适的位置.
    2.从第二个位置开始, 把第二个位置的数字和第一个位置的数字比较, 决定交换与否以此类推
    3.交换可以从前往后找, 也可以从后往前找,这里的前后指的是已经排好顺序的部分.
    4.上述的过程也可以是倒过来的, 意思是最后的位置是排好的, 然后把数字往后面插.
    5.所以说, 有一部分排好了, 不管是前边的排好了, 还是后边的排好了用插入
    6.外层确定循环次数,同时指定了待插入的数字的位置
    7.内层执行插入, 从哪个方向插都行, 看情况, 这里就从左往右吧. 俩中方法的交换次数一样, 判断次数有不太一样.
    8.外层n内层最坏是n, 所以最坏时间复杂度O(n^2)n=len()-1
"""


# 这里使用的逻辑是把小于待插数字的数字和待插数交换之后处于待插数位置的数字就一直
# 小于内层遍历的位置的数字, 就会一直交换到内层循环结束.
def insert_sort1(unsort):
    n = len(unsort)
    # 决定循环次数, 指定代插入数字的位置
    for i in range(1, n):
        for j in range(0, i):
            if unsort[i] < unsort[j]:
                unsort[j], unsort[i] = unsort[i], unsort[j]
            # 这里不能使用else:break, 应为要从左往右寻找到第一个大于待插数的位置.
    return unsort


# 这里的内层循环更像是使用了冒泡排序法.就叫它插入冒泡法吧.
def insert_sort2(unsort):
    n = len(unsort)
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if unsort[j + 1] < unsort[j]:
                unsort[j + 1], unsort[j] = unsort[j], unsort[j + 1]
            # 这里当然可以使用退出
            else:
                break
    return unsort


if __name__ == '__main__':
    from test_sort import test_sort_algorithm

    print('插入排序1(从左到右)')
    test_sort_algorithm(insert_sort1)
    print('插入排序2(从右到左)')
    test_sort_algorithm(insert_sort2)
