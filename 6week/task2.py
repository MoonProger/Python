"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/repeated-dna-sequences/description/
"""

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []

        orig = set()
        twin = set()

        for i in range(len(s) - 9):
            substr = s[i:i + 10]
            if substr in orig:
                twin.add(substr)
            else:
                orig.add(substr)

        return list(twin)
