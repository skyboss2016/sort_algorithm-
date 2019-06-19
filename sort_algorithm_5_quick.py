"""
快速排序法:
    1.快速排序法属于交换类的排序方法, 和冒泡排序法都是交换类.
    2.基本原则是选定一个数字, 然后将代排序列表中的所有小于选定数字的放到左边, 大于选定数字的放到右边
    3.对选定数字左右两边排好序的内容, 在执行2.
    4.大于的数字放到左边就是从大到小排序了.
    5.本次排序使用的方法:
        o 将列表的左右俩端索引赋值给left, right
        o 从右向左判断如果当前值大于选定值, right减一, 否则交换选定的位置和当前right位置的值
        o 接着从左向右判断如果当前值小于选定值, left加一, 否则交换选定位置和当前left位置的值
        o 交换结束时left, right, 选定位置应当是同一个值
        o 左边序列和右边序列传分别执行1,2,3步骤.
    6.标准的排序方法应当是:

"""


def quick_sort(unsort):
    first = 0
    last = len(unsort) - 1
    inner_sort(unsort, first, last)


def inner_sort(unsort, first, last):
    if first >= last:
        return
    left = pivot = first
    right = last
    while left <= right:
        while left <= right:
            if unsort[right] >= unsort[pivot]:
                right -= 1
            else:
                unsort[right], unsort[pivot] = unsort[pivot], unsort[right]
                pivot = right
                break

        while left < right:
            if unsort[left] <= unsort[pivot]:
                left += 1
            else:
                unsort[left], unsort[pivot] = unsort[pivot], unsort[left]
                pivot = left
                break

    inner_sort(unsort, first, pivot - 1)
    inner_sort(unsort, pivot + 1, last)


def quick_sort2(unsort):
    first = 1
    last = len(unsort) - 1
    inner_sort2(unsort, first, last)


def inner_sort2(unsort, first, last):
    if first >= last:
        return
    left = first
    right = last
    pivot = unsort[first]
    while left < right:
        while left < right and unsort[right] >= pivot:
            unsort[first] = pivot


    inner_sort(unsort, first, pivot - 1)
    inner_sort(unsort, pivot + 1, last)


if __name__ == '__main__':
    from test_sort import test_sort_algorithm

    # print('我理解的方法.')
    # test_sort_algorithm(quick_sort)
    print('更好的方法.')
    test_sort_algorithm(quick_sort2, once=True)