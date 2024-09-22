"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""

class Solution(object):
    def letterCombinations(self, digits):
        res = []
        dict = [''] * 11
        dict[2] = 'abc'
        dict[3] = 'def'
        dict[4] = 'ghi'
        dict[5] = 'jkl'
        dict[6] = 'mno'
        dict[7] = 'pqrs'
        dict[8] = 'tuv'
        dict[9] = 'wxyz'


        if len(digits) == 1:
            for i in dict[int(digits[0])]:
                res.append(i)

        elif len(digits) == 2:
            for i in dict[int(digits[0])]:
                for j in dict[int(digits[1])]:
                    res.append(i + j)

        elif len(digits) == 3:
            for i in dict[int(digits[0])]:
                for j in dict[int(digits[1])]:
                    for k in dict[int(digits[2])]:
                        res.append(i + j + k)

        elif len(digits) == 4:
            for i in dict[int(digits[0])]:
                for j in dict[int(digits[1])]:
                    for k in dict[int(digits[2])]:
                        for p in dict[int(digits[3])]:
                            res.append(i + j + k + p)
        else:
            return []

        return res
