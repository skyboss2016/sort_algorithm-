def bubble_sort(alist: list):
    n = len(alist)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
    return alist


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(li)
    print(li)
