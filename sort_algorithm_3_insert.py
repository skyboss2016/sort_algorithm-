"""
插入排序法:
    1.插入类排序, 同类排序还有折半插入排序, 希尔排序
    2.基本思路就像是整理扑克牌, 从左往右把牌依次插到左边合适的位置.
    3.从第二个位置开始, 把第二个位置的数字和第一个位置的数字比较, 决定交换与否, 之后的以此类推
    4.交换可以从前往后找, 也可以从后往前找,这里的前后指的是已经排好顺序的部分.
    5.上述的过程也可以是倒过来的, 意思是最后的位置是排好的, 然后把数字往后面插.
    6.所以说, 有一部分排好了, 不管是前边的排好了, 还是后边的排好了用插入
    7.外层确定循环次数,同时指定了待插入的数字的位置
    8.内层执行插入, 从哪个方向插都行, 看情况, 俩中方法的交换次数一样, 比较判断次数不一样.
    9.外层n内层最坏是n, 所以最坏时间复杂度O(n^2)

    10.折半插入排序, 使用折半查找相近的思路, 重点是找到应该插入的位置,
    11.查找方法就是找区间, 待插值小于中间值就把区间换到当前区间开始到中间值之前,然后再次折半查找
    12.为了方便表述F代区间开始下标索引, M代表中间, B代表区间结束下标
    13.最后会到一个[F M B](区间开始, 区间中间, 区间结束, 三者相邻的状态).
    14.一个值的思考的情况是中间值和待插入值相等的情况.不考虑这种情况在使用while时就会陷入死循环
    15.while的判断条件F<=B. 这时最终的结果是[MB F](MB相等, F在右侧)这时F就表示该往哪儿插,该怎么交换就参考代码吧
    16.while判断条件可以改为F<B, 不过这会带来一定的不明确因为这是情况变成了[FMB](F=M=B), 这时他们的右侧就是该插入位置
    17.[FMB]情况,中间值等于待插值这种情况划到待插值大于中间值的情况里, 总之就是让F往后移动.
    18.时间复杂度,O(n^2)
"""


# 这里使用的逻辑是把小于待插数字的数字和待插数交换之后处于待插数位置的数字就一直
# 小于内层遍历的位置的数字, 就会一直交换到内层循环结束.
def insert_sort1(unsort):
    n = len(unsort)
    # 决定循环次数, 指定代插入数字的位置
    for i in range(1, n):
        for j in range(i):
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


# 这个运算速度最快
def insert_sort3(unsort):
    n = len(unsort)
    for i in range(1, n):
        while i > 0 and unsort[i] < unsort[i - 1]:
            unsort[i], unsort[i - 1] = unsort[i - 1], unsort[i]
            i -= 1


# 折半插入排序
def binary_insert_sort(unsort):
    n = len(unsort)
    for i in range(1, n):
        front = 0
        back = i - 1
        while front <= back:
            mid = (front + back) // 2
            if unsort[i] <= unsort[mid]:
                back = mid - 1
            else:
                front = mid + 1
        for j in range(front, i):
            unsort[j], unsort[i] = unsort[i], unsort[j]
    return unsort


if __name__ == '__main__':
    from test_sort import test_sort_algorithm

    print('插入排序1(从左到右)')
    test_sort_algorithm(insert_sort1)
    print('插入排序2(从右到左)')
    test_sort_algorithm(insert_sort2)
    print('折半插入排序')
    test_sort_algorithm(binary_insert_sort)
    print('插入排序3(从右到左) while')
    test_sort_algorithm(insert_sort3)
