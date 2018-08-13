def merge_sort(alist):
    n = len(alist)

    if n == 1:
        return alist

    mid = n // 2

    sort_list = []

    left_list = merge_sort(alist[:mid])
    right_list = merge_sort(alist[mid:])

    l, r = 0, 0
    ln, rn = len(left_list), len(right_list)
    print(left_list, right_list)
    while l < ln and r < rn:
        if left_list[l] > right_list[r]:
            sort_list.append(right_list[r])
            r += 1
        else:
            sort_list.append(left_list[l])
            l += 1
    sort_list += left_list[l:]
    sort_list += right_list[r:]

    return sort_list


if __name__ == '__main__':
    alist = [12, 34, 56, 78, 90, 98, 76, 54, 32, 21]
    result = merge_sort(alist)
    print(alist)
    print(result)
