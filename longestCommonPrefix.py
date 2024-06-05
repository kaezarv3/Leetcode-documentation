
#https://leetcode.com/problems/longest-common-prefix/description/

# ''' Write a function to find the longest common prefix string amongst an array of streams. 
#     If there is no common prefix, return an empty string
# '''

# I feel like this falls into the category of sliding window problems. Just based off of the "common prefix section"
# Prefix is another word for substring. So yeah. 

def longestCommonPrefix(strs: list[str]) -> str:
    dicty = {}
    dictlist = []
    smallestWord = min(len(ele) for ele in strs)
    for i in range(smallestWord):
        # print(i)
        dictlist = []
        for item in strs:
            mvp = item[i]
            dicty[i] = mvp
            dictlist.append(dicty)
            print(dictlist)
            if len(dictlist) > 1:
                print(all(x == dictlist[0] for x in dictlist[1:]))

        print("-"*50)

strs = ["flower","flow","flight","flopper","flounder"]
longestCommonPrefix(strs) 


    



