"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_len = 0
        for i in range(len(s)):
            flag = True
            for j in range(i+1, len(s)+1):
                str = s[i:j]
                if str.count(str[-1]) > 1:
                    flag = False
                    break

                if flag == False:
                    break
                else:
                    max_len = max(max_len, len(str))
        return max_len