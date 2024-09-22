"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_len = 0
        for i in range(len(s)):
            flag = True
            for j in range(i+1, len(s)+1):
                stroka = s[i:j]
                if stroka.count(stroka[-1]) > 1:
                    flag = False
                    break

                if flag == False:
                    break
                else:
                    max_len = max(max_len, len(stroka))
        return max_len
