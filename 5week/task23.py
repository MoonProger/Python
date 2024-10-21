"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/fraction-to-recurring-decimal/description/
"""


class Solution(object):
    def fractionToDecimal(self, numer, denom):
        if numer == 0:
            return "0"

        res = []

        if (numer < 0) != (denom < 0):
            res.append("-")
        numer = abs(numer)
        denom = abs(denom)

        res.append(str(numer // denom))
        ost = numer % denom
        if ost == 0:
            return "".join(res)

        res.append(".")
        ost_positions = {}

        while ost != 0:
            if ost in ost_positions:
                res.insert(ost_positions[ost], "(")
                res.append(")")
                break

            ost_positions[ost] = len(res)

            ost *= 10
            res.append(str(ost // denom))
            ost %= denom

        return "".join(res)

