class Solution:
    def __init__(self):
        self.stack = []
        self.left_brackets = ['(', '[', '{']
        self.right_brackets = [')', ']', '}']
        self.brackets_map = dict(zip(self.left_brackets, self.right_brackets))


    def isValid(self, s: str) -> bool:
        if not s:
            return True
        if len(s) == 1 or s[0] in self.right_brackets:
            return False
        for c in s:
            if c in self.left_brackets:
                self.stack.append(c)
            elif c in self.right_brackets:
                if not self.stack:
                    return False
                left = self.stack.pop()
                if self.brackets_map[left] == c:
                    continue
                else:
                    return False
        if self.stack:
            return False
        else:
            return True



if __name__ == '__main__':
    solution = Solution()
    result = solution.isValid('{[]}')
    print(result)
