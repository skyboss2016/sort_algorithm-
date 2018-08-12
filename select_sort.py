def select_sort(alist):
    n = len(alist)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n - 1):
            if alist[j] < alist[min_index]:
                min_index = j

        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    select_sort(li)
    print(li)
