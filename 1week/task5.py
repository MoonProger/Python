"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/group-anagrams/description/
"""



class Solution(object):
    def groupAnagrams(self, strs):
        res = {}

        for s in strs:
            sort_s = "".join(sorted(s))
            #print(sort_s)
            if sort_s in res:
                res[sort_s].append(s)
            else:
                res[sort_s] = [s]

        return list(res.values())



#n = ["eat","tea","tan","ate","nat","bat"]
#solution = Solution()
#print(solution.groupAnagrams(n))
