class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"

        prev = self.countAndSay(n - 1)
        res = ""
        count = 1
        length = len(prev)

        for i in range(1, length):
            if prev[i] == prev[i - 1]:
                count += 1
            else:
                res += str(count) + prev[i - 1]
                count = 1

        res += str(count) + prev[-1]

        return res