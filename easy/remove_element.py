class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        while val in nums:
            nums.remove(val)

        return len(nums)


if __name__ == '__main__':
    solution = Solution()
    nums = [3,2,2,3]
    val = 3
    result = solution.removeElement(nums, val)
    print(result)
