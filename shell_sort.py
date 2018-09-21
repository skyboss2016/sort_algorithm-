def shell_sort(alist):
    n = len(alist)
    gep = n // 2
    while gep > 0:
        for i in range(gep, n):
            # print(i)
            while i - gep >= 0 and alist[i] < alist[i - gep]:
                alist[i], alist[i - gep] = alist[i - gep], alist[i]
                print('a')
                i -= gep
        gep //= 2
    return alist


if __name__ == '__main__':
    # li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # li = [13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10]
    li = [10, 13, 14, 23, 25, 25, 27, 33, 39, 45, 59, 65, 73, 82, 94, 94]
    # li.reverse()
    shell_sort(li)
    print(li)

