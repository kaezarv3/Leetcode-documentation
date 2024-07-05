
# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         # Item[i] is the key, and value is resulting value in answer field index in list
#         hashy = {}
#         for i in range(len(nums)):
#             # For each iteration of this loop
#             curr = 1
#             for item in nums:
#                 if (str(i) not in hashy):
#                     hashy[str(i)] = curr 
#                 if item != nums[i] and (str(i) in hashy):
#                     # If the item is not the selected item and the index position is in the hash table multiply it, if its empty start with 0
#                     curr = curr * item
#                     hashy[str(i)] = curr
#         res = []
#         for num in hashy.values():
#             res.append(num) 
#         return res

# sol = Solution()
# inp = [1,2,3,4]
# inp = [0,0]
# print(sol.productExceptSelf(inp))



# This solution uses a left and right prefix algorithm to solve. 
# Basiclly break it up into solving for left and right side of an index in a list and then boom problem solved kinda

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            # Starting backwards from the end of the list 
            res[i] *= postfix
            # Change the results in the result list 
            postfix *= nums[i]
            # keep it going. Problem is better understood now
        return res


                    
            



# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]



            
            