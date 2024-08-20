# https://leetcode.com/problems/two-sum/

class Solution:
    def two_Sum(self, nums: list[int], target: int) -> list[int]:
        output = []
        for num in nums:
            if len(nums) - 1 != nums.index(num):
                for i in range(nums.index(num), len(nums) - 1):
                    if num + nums[i + 1] == target:
                        if nums.index(num) not in output:
                            output.append(nums.index(num))
                        if i + 1 not in output:
                            output.append(i + 1)
        return output