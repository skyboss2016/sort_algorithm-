def insert_sort(alist):
    n = len(alist)

    for i in range(1, n):
        for j in range(i, 0, -1):  # 错误点: (i, 1, -1), 第二个数是用来判断的达不到的.应当为0,此时计数到1为止就不再继续进行了.
            if alist[j] < alist[j - 1]:   # 错误点: > 理论是当前边的数字大于后边的数字时交换位置升序排列,现在只考虑升序.
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
            else:
                break

    return alist


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insert_sort(li)
    print(li)
