# -*- coding:utf-8 -*-
"""
    filename:       palindrome_number
    description:    django learning practice
    author:         xiezh
    date:           2019/4/1
"""
__author__ = 'xiezh'


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        origin_list = list(str(x))
        if len(origin_list) == 1:
            return True
        elif origin_list[len(origin_list) - 1] == '0':
            return False
        reversed_list = origin_list.copy()
        reversed_list.reverse()
        return origin_list == reversed_list


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(123))