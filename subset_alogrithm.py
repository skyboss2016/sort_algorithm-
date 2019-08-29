# -*- coding: utf-8 -*-
"""
# 编写一个递归函数,该函数将输出一个含有n个元素的集合的所有子集(没有任何重复的子集)
Start by removing the first element x and computing all the subsets that don’t contain x.
*1:在进行到n = len(s) - 1这一步时传递到下一层的内容是n+1,并且会return到上一层,不会执行到n = len(s).
所以不会出现list index out of range的错误.
*2:i=len(s)因为match的长度和s是相同的,
"""


# 方法一
# 使用二进制对对应数字匹配的方法.
def subset1(s):
    def inner(n, i):
        if n == i:
            ret = []
            for j in range(len(s)):
                if match[j] == 1:
                    ret.append(s[j])
            print(ret)
            return
        match[n] = 0
        inner(n + 1, i)  # *1
        match[n] = 1
        inner(n + 1, i)

    match = [0] * len(s)
    inner(0, len(s))  # *2


# 方法二
# 截取出第一个元素, 计算剩下的集合的所有子集, 将所有子集复制一遍给每一个子集结果添加之前截取出的元素.
def subset2(s):
    if len(s) <= 0:
        return [[]]
    font = s.pop()
    result = subset2(s)
    length = len(result)
    for num in range(length):
        m = result[num].copy()
        m.append(font)
        result.append(m)
    return result


if __name__ == '__main__':
    subset1(['a', 'b', 'c', 'd'])
    print(subset2(['a', 'b', 'c', 'd']))
