import random
from itertools import permutations


def test_sort_algorithm(sort_func, *, once=False, specify_list=None, list_len=9):
    """
    测试排序算法函数
    :param sort_func: 排序算法函数
    :type sort_func: function
    :param list_len: 指定自动生成的列表长度, 当sort_list指定时实效
    :type list_len: int
    :param once: 只执行一次
    :type once: bool
    :param specify_list: 指定排序列表
    :type specify_list: list
    :return: None
    """
    sort_list = specify_list or [random.randint(11, 99) for _ in range(list_len)]
    if once:
        print('原始排序:', sort_list)
        print('*' * 80)
        compare_list = sort_list.copy()
        sort_func(sort_list)
        compare_list.sort()
        if sort_list != compare_list:
            print('错误的排序:', sort_list)
            print('正确的排序:', compare_list)
        else:
            print('测试通过:结果:', sort_list)
    else:
        test_lists = permutations(sort_list)
        for temp_tuple in test_lists:
            test_list = list(temp_tuple)
            compare_list = test_list.copy()
            backup_list = test_list.copy()
            sort_func(test_list)
            compare_list.sort()
            if test_list != compare_list:
                print('原始排序:', backup_list)
                print('*' * 80)
                print('错误的排序:', sort_list)
                print('正确的排序:', compare_list)
                print('#' * 80)
                break
        else:
            print('测试通过')
