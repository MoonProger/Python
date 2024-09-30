class Solution(object):
    def compareVersion(self, version1, version2):
        v1_splited = version1.split(".")
        v2_splited = version2.split(".")
        max_length = max(len(v1_splited), len(v2_splited))

        for i in range(max_length):
            if i < len(v1_splited):
                v1 = int(v1_splited[i])
            else:
                v1 = 0

            if i < len(v2_splited):
                v2 = int(v2_splited[i])
            else:
                v2 = 0

            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1

        return 0