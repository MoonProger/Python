"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/multiply-strings/description/
"""

class Solution(object):
    def multiply(self, num1, num2):
        mid_calculations = []

        ind2 = len(num2) - 1
        while ind2 >= 0:
            ind1 = len(num1) - 1
            mid = ""
            ost = 0
            while ind1 >= 0:
                if ind1 == 0:
                    mid = str((int(num1[ind1]) * int(num2[ind2])) + ost) + mid
                else:
                    mid = str((int(num1[ind1]) * int(num2[ind2])) + ost)[-1] + mid
                    ost = (int(num1[ind1]) * int(num2[ind2]) + ost) // 10

                #print(num1[ind1],num2[ind2], "--", mid, ost)
                ind1 -= 1
            mid_calculations += [mid]
            #print(mid)
            ind2 -= 1

        res = 0
        multiplyer = 1
        for i in range(len(mid_calculations)):
            res += int(mid_calculations[i]) * multiplyer
            multiplyer *= 10
        return str(res)

  
