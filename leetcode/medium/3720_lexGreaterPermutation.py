import json
from collections import Counter
from functools import cache
from typing import List

"""
1) left part is equal
2) res[id] > target[id]
3) right part sorted in non decreasing order
4) id should be right as possible

1) different chars
abc, bba = bca

2) equal chars
aabb, baba = bbaa
aabb, bbaa = ''



"""


class Solution:
    def isEqual(self):
        for i in range(26):
            if self.sCnt[i] != self.tCnt[i]:
                return False
        return True

    def processNotEqual(self):
        res = []
        for i in range(self.N):
            char = self.target[i]
            code = ord(char) - self.oa
            if self.sCnt[code] != 0:
                res.append(char)
                self.sCnt[code] -= 1
            else:
                break

        maxCode = -1
        for i in range(25, -1, -1):
            if self.sCnt[i] != 0:
                maxCode = i
                break

        while len(res) or maxCode + self.oa > ord(self.target[len(res)]):
            if maxCode + self.oa > ord(self.target[len(res)]):
                mc = -1
                for i in range(26):
                    if self.sCnt[i] != 0 and self.oa + i > ord(self.target[len(res)]):
                        mc = i
                        break
                res.append(chr(self.oa + mc))
                self.sCnt[mc] -= 1
                break
            else:
                char = res.pop()
                code = ord(char) - self.oa
                self.sCnt[code] += 1
                maxCode = max(maxCode, code)

        if len(res) == 0:
            return ""

        for i in range(26):
            if self.sCnt[i] != 0:
                char = chr(i + self.oa)
                res.append(char * self.sCnt[i])

        return "".join(res)

    def processEqual(self):
        maxCode = -1
        id = -1
        codes = [0] * 26

        for i in range(self.N - 1, -1, -1):
            char = self.target[i]
            code = ord(char) - self.oa

            if maxCode > code:
                id = i
                break

            codes[code] += 1
            maxCode = max(maxCode, code)

        if id == -1:
            return ""

        for i in range(26):
            if codes[i] != 0 and self.oa + i > ord(self.target[id]):
                maxCode = i
                break

        res = []

        # print("id", id, "maxCode", maxCode)

        for i in range(self.N):
            if id == i:
                char = chr(maxCode + self.oa)
                self.sCnt[maxCode] -= 1
                res.append(char)
                break

            char = self.target[i]
            code = ord(char) - self.oa
            self.sCnt[code] -= 1

            res.append(char)

        # print("res", res)

        for i in range(26):
            if self.sCnt[i] != 0:
                char = chr(i + self.oa)
                res.append(char * self.sCnt[i])

        return "".join(res)

    def lexGreaterPermutation(self, s: str, target: str) -> str:
        self.s = s
        self.target = target
        self.N = len(s)
        self.oa = ord("a")
        self.sCnt = [0] * 26
        self.tCnt = [0] * 26

        for i in range(self.N):
            code = ord(s[i]) - self.oa
            self.sCnt[code] += 1

            code = ord(target[i]) - self.oa
            self.tCnt[code] += 1

        if self.isEqual():
            return self.processEqual()

        return self.processNotEqual()


def test():
    params = [
        {
            "input": ["abc", "bba"],
            "output": "bca",
        },
        {
            "input": ["leet", "code"],
            "output": "eelt",
        },
        {
            "input": ["baba", "bbaa"],
            "output": "",
        },
        {
            "input": ["bbaa", "baba"],
            "output": "bbaa",
        },
        {
            "input": ["bbaa", "aabb"],
            "output": "abab",
        },
        {
            "input": ["aba", "aca"],
            "output": "baa",
        },
        {
            "input": ["ab", "ab"],
            "output": "ba",
        },
        {
            "input": [
                "abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde",
                "edcbaedcbaedcbaedcbaedcbaedcbaedcbaedcbaedcbaedcba",
            ],
            "output": "edcbaedcbaedcbaedcbaedcbaedcbaedcbaedcbaedcbbaacde",
        },
    ]
    solution = Solution()

    for param in params:
        s, target = param["input"]
        result = solution.lexGreaterPermutation(s, target)
        correct = json.dumps(result) == json.dumps(param["output"])

        msg = "SUCCESS" if correct else "ERROR"
        msg += "\n"
        if not correct:
            msg += "input " + json.dumps(param["input"]) + "\n"
            msg += "output " + json.dumps(param["output"]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

        print(msg)


if __name__ == "__main__":
    test()
