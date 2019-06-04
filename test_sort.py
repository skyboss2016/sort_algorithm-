import random
from itertools import permutations


def test_sort_algorithm(sort_func, list_len=9):
    """
    测试排序算法函数
    :param sort_func:
    :type sort_func: function
    :param list_len:
    :type list_len: int
    :return:
    """
    sort_list = [random.randint(11, 99) for _ in range(list_len)]
    print('原始排序:', sort_list)
    compare_list = sort_list.copy()
    back_list = sort_list.copy()

    sort_func(sort_list)
    compare_list.sort()
    if sort_list != compare_list:
        print('错误的排序:', sort_list)
        print('正确的排序:', compare_list)
    else:
        print('排序正确:', sort_list)

    test_lists = permutations(back_list, len(back_list))
    for temp_tuple in test_lists:
        test_list = list(temp_tuple)
        compare_list = test_list.copy()

        sort_func(test_list)
        compare_list.sort()
        if test_list != compare_list:
            print('-' * 80)
            print('错误的排序:', sort_list)
            print('正确的排序:', compare_list)
            print('#' * 80)
        # else:
        #     print('ok')
