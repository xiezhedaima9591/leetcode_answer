# -*- coding:utf-8 -*-
"""
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−231,  231 − 1].
For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.
"""
__author__ = 'xiezh'


class Solution:
    def reverse(self, x: int) -> int:
        negative = False if x >= 0 else True
        if negative:
            x = -x
        x = list(str(x))
        x.reverse()
        x = int(''.join(x))
        if negative:
            x = -x
        if x < pow(-2, 31) or x > pow(2, 31) - 1:
            return 0
        return x


if __name__ == '__main__':
    solution = Solution()
    x = 1534236469
    print(x)
    x = solution.reverse(x)
    print(x)
