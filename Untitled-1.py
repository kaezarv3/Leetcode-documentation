"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        res = []
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if numbers[j] == numbers[i]:
                    continue
                if numbers[j] + numbers[i] == target:
                    res.append(i + 1)
                    res.append(j + 1)
                    return res

numbers = [2,7,11,15]
target = 9

sol = Solution()
print(sol.twoSum(numbers, target))