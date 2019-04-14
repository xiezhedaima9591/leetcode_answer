class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            position = haystack.index(needle)
        except ValueError:
            return -1
        return position


if __name__ == '__main__':
    solution = Solution()
    h = 'aaaaa'
    n = 'bba'
    result = solution.strStr(h, n)
    print(result)
