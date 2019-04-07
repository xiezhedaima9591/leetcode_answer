# -*- coding:utf-8 -*-
"""
    filename:       longest_common_prefix
    description:    django learning practice
    author:         xiezh
    date:           2019/4/7
"""
__author__ = 'xiezh'
from functools import reduce


class Solution:
    def longest_common_prefix(self, strs: list) -> str:
        if not strs:
            return ''
        common_prefix = reduce(self.find_common, strs)
        return common_prefix

    def find_common(self, str1: str, str2: str) -> str:
        max_len = len(str1) if len(str1) < len(str2) else len(str2)
        result = ''
        for i in range(max_len):
            if str1[i] == str2[i]:
                result += str1[i]
            else:
                return result
        return result


if __name__ == '__main__':
    solution = Solution()
    prefix = solution.longest_common_prefix(["dog", "racecar", "car"])
    print(prefix)
