# -*- coding:utf-8 -*-
"""
    filename:       roman_to_integer
    description:    django learning practice
    author:         xiezh
    date:           2019/4/2
"""
__author__ = 'xiezh'


class Solution:
    def roman_to_int(self, s: str) -> int:
        map_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_list = list(s)
        int_list = list(map(lambda c: map_dict[c], roman_list))
        result = 0
        before = int_list[len(int_list) - 1]
        for i in range(len(int_list) - 1, -1, -1):
            result += (-int_list[i] if int_list[i] < before else int_list[i])
            before = int_list[i]
        return result


if __name__ == '__main__':
    roman = input('input roman number: ')
    solution = Solution()
    re = solution.roman_to_int(roman)
    print(re)

