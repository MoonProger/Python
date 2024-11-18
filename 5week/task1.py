"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/integer-to-roman/description/
"""

class Solution(object):
    def intToRoman(self, num):
        rom_num = ''

        while num >= 1000:
            rom_num += 'M'
            num -= 1000

        while num >= 900:
            rom_num += 'CM'
            num -= 900

        while num >= 500:
            rom_num += 'D'
            num -= 500

        while num >= 400:
            rom_num += 'CD'
            num -= 400

        while num >= 100:
            rom_num += 'C'
            num -= 100

        while num >= 90:
            rom_num += 'XC'
            num -= 90

        while num >= 50:
            rom_num += 'L'
            num -= 50

        while num >= 40:
            rom_num += 'XL'
            num -= 40

        while num >= 10:
            rom_num += 'X'
            num -= 10

        while num >= 9:
            rom_num += 'IX'
            num -= 9

        while num >= 5:
            rom_num += 'V'
            num -= 5

        while num >= 4:
            rom_num += 'IV'
            num -= 4

        while num >= 1:
            rom_num += 'I'
            num -= 1

        return rom_num