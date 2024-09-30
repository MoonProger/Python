class Solution(object):
    def partition(self, s):
        stack = [(0, [])]
        res = []

        while stack:
            flag = 1
            start, path = stack.pop()

            if start == len(s):
                res.append(path)
                flag = 0

            if flag == 1:
                for end in range(start + 1, len(s) + 1):
                    substr = s[start:end]
                    if substr == substr[::-1]:
                        stack.append((end, path + [substr]))

        return res