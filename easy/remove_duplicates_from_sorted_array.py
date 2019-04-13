class Solution:
    def removeDuplicates(self, nums: list) -> int:
        distinct_nums = sorted(list(set(nums)))
        nums.clear()
        nums.extend(distinct_nums)
        return len(nums)


if __name__ == '__main__':
    solution = Solution()
    num_list = [0,0,1,1,1,2,2,3,3,4]
    result = solution.removeDuplicates(num_list)
    print(result)
