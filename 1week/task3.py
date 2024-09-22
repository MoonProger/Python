"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-palindromic-substring/description/
"""


class Solution(object):
    def longestPalindrome(self, s):
        if len(s) == s.count(s[0]):
            return s
        max_len = 0
        res = ""

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                stroka = s[i:j]
                if stroka == stroka[::-1]:
                    if len(stroka) > max_len:
                        max_len = len(stroka)
                        res = stroka

        return res if res else s[0]
