# 347. Top K Frequent Elements, 

""" 
    Given an integer array nums and an integer k, 
    return the k most frequent elements. 
    You may return the answer in any order.

    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

"""
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Creates Dictionary for storing frequency 
        dicty = {}
        # This section counts the number of times a specific element appears in a list using a dictionary
        for i in range(len(nums)):
            curr = nums[i]
            if curr in dicty:
                dicty[curr] += 1
            else:
                dicty[curr] = 1
        # Then I sort the list of tuples from dicty.items in reverse, by the second element in the tuples in the list. "Hence a:a[1]"
        res = sorted(dicty.items(), key= lambda a:a[1], reverse=True)
        res_list = []

        # Here I append res[i][0] for every value up to k to return the answer, which is the top "K" keys of the dictionary. 
        for i in range(k):
            res_list.append(res[i][0])
        
        return res_list
    
sol = Solution()

nums = [1,1,1,2,2,2,3,3,3,3,3,4,4,4,4,4]
k = 3

print(sol.topKFrequent(nums,k))


        

