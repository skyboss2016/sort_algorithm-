def quick_sort(alist, start, stop):
    # print(start,stop)
    if start >= stop:
        return

    left = start
    right = stop

    mid = alist[start]

    while left < right:
        # print(left, right)
        while left < right and alist[right] >= mid:
            right -= 1

        alist[left] = alist[right]

        while left < right and alist[left] <= mid:
            left += 1

        alist[right] = alist[left]
        #  2     0
    # print(left, right)
    assert left == right, ''

    alist[left] = mid

    quick_sort(alist, start, left - 1)
    quick_sort(alist, left + 1, stop)
    # return alist


if __name__ == '__main__':
    # li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    li = [13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10]
    quick_sort(li, 0, len(li) - 1)
    print(li)
