"""
快速排序法:
    1.快速排序法属于交换类的排序方法, 和冒泡排序法都是交换类.
    2.基本原则是选定一个数字, 然后将代排序列表中的所有小于选定数字的放到左边, 大于选定数字的放到右边
    3.对选定数字左右两边排好序的内容, 在执行2.
    4.大于的数字放到左边就是从大到小排序了.
    5.第一个排序使用的方法:
        一 将列表的左右俩端索引赋值给left, right
        二 从右向左判断如果当前值是否大于选定值, 是right减一, 否则交换选定的位置和当前right位置的值
        三 接着从左向右判断如果当前值是否小于选定值, 是left加一, 否则交换选定位置和当前left位置的值
        四 交换结束时left, right, 选定位置应当是同一个值
        五 左边序列和右边序列传分别执行1,2,3步骤.

        * 开头是选定值, 先从右边开始往左找小于选定值的数字和左边(此时是开头)交换, 修改选定位置的索
        引. 然后从最左边开始往右找, 找到大于选定值的数字和右边(此时是之交换时的位置)交换, 然后再从
        右向左搜寻小于选定值的数字和左边交换, 如此往复,记住每次交换完更改选定值的索引. 直到左右选
        定值索引是一个数字, 然后把选定值左边序列, 右边序列再执行上述操作.
    6.另一种方法:
        * 还是把第一个值设定为选定值, 然后保存这个值, 然后从右往左找,找到小于选定值的就把值赋给
        左边(left指定的值, 首次覆盖的是第一个值,就是选定的值,保存了的值), 然后在从左往右找, 把
        找到的第一个大于选定值的值赋给右边(right指定的值, 就是刚才把值赋给了左边的那个值)之后再
        从右边向左找, 找小于选定值的值然后赋值给左边,如此循环往复直到左右相等. 这时再把保存的值
        赋给left或right(这俩相等了).
    7.方法三:
        * 设置一个选定值, 赋给变量(上述为保存起来), 然后把值和结尾的值交换, 然后设置boundary为
        left, 即左边的值, 之后for循环, 把所有小于选定值的数字和boundary交换, 接着boundary += 1
        准备和for循环后边的数字交换, 循环结束后, 把之前和结尾交换的值, 和boundary交换回来. 把
        boundary之前和之后的列表, 重新传递进来, 执行这个步骤.
    8.注意选定值不能为数字, 千万不要写数字, 写成left, right, 或(left + right) // 2 或者其他
    的表达式的值, 千万不能是数字


"""


def quick_sort(unsort_list):
    start = 0
    finish = len(unsort_list) - 1

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

    inner_sort(unsort_list, start, finish)


def quick_sort2(unsort_list):
    start = 0
    finish = len(unsort_list) - 1

    def inner_sort(unsort, first, last):
        if first >= last:
            return
        left = first
        right = last
        pivot = unsort[first]
        while left < right:
            while left < right and unsort[right] >= pivot:
                right -= 1
            unsort[left] = unsort[right]
            while left < right and unsort[left] <= pivot:
                left += 1
            unsort[right] = unsort[left]
        unsort[right] = pivot
        inner_sort(unsort, first, right - 1)
        inner_sort(unsort, right + 1, last)

    inner_sort(unsort_list, start, finish)


def quick_sort3(unsort_list):
    start = 0
    finish = len(unsort_list) - 1

    def inner_sort(unsort, left, right):
        if left >= right:
            return
        # middle = left      # middle的值可以设为left, right, 或(left + right) // 2
        # middle指定的就是下边的left,
        pivot = unsort[left]
        unsort[left], unsort[right] = unsort[right], unsort[left]
        boundary = left
        for i in range(left, right):
            if unsort[i] < pivot:
                unsort[i], unsort[boundary] = unsort[boundary], unsort[i]
                boundary += 1
        unsort[boundary], unsort[right] = unsort[right], unsort[boundary]

        inner_sort(unsort, left, boundary - 1)
        inner_sort(unsort, boundary + 1, right)

    inner_sort(unsort_list, start, finish)


if __name__ == '__main__':
    from test_sort import test_sort_algorithm

    print('我理解的方法.')
    test_sort_algorithm(quick_sort)
    print('另一种方法.')
    test_sort_algorithm(quick_sort2)
    print('第三种方法.')
    test_sort_algorithm(quick_sort3)
