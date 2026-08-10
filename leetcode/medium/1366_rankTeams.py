import math
from collections import defaultdict, deque
from functools import cache
from json import dumps
from typing import List


class Solution_0:
    def rankTeams(self, votes: List[str]) -> str:
        M = len(votes[0])

        places = [defaultdict(int) for i in range(M)]
        total = [0] * 26

        for word in votes:
            for i in range(M):
                char = word[i]
                places[i][char] += 1
                total[ord(char) - ord("A")] += 26 - i

        # print(places)

        used = [0] * 26
        res = ""
        for i in range(M):
            # print("places[i].items()", places[i].items())

            arr = [
                (char, num, total[ord(char) - ord("A")])
                for char, num in places[i].items()
            ]

            # print(1, "arr", arr)

            arr = sorted(arr, key=lambda x: (-x[1], -x[2], x[0]))
            # arr = [("W", 1), ("X", 1)]

            # print(2, "arr", arr)

            for char, cnt, scores in arr:
                if used[ord(char) - ord("A")] == 1:
                    continue
                used[ord(char) - ord("A")] = 1
                res += char

        return res


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        M = len(votes[0])

        chars = {}
        for vote in votes:
            for i in range(M):
                char = vote[i]
                if char not in chars:
                    chars[char] = [0] * 26
                chars[char][i] += 1

        arr = [(tuple(-s for s in scores), char) for char, scores in chars.items()]

        # print(1, arr)

        arr = sorted(arr)

        res = [v[1] for v in arr]

        # print(res)

        return "".join(res)


def test():
    params = [
        {
            "input": ["ABC", "ACB", "ABC", "ACB", "ACB"],
            "output": "ACB",
        },
        {
            "input": ["WXYZ", "XYZW"],
            "output": "XWYZ",
        },
        {
            "input": ["ZMNAGUEDSJYLBOPHRQICWFXTVK"],
            "output": "ZMNAGUEDSJYLBOPHRQICWFXTVK",
        },
        {
            "input": [
                "FVSHJIEMNGYPTQOURLWCZKAX",
                "AITFQORCEHPVJMXGKSLNZWUY",
                "OTERVXFZUMHNIYSCQAWGPKJL",
                "VMSERIJYLZNWCPQTOKFUHAXG",
                "VNHOZWKQCEFYPSGLAMXJIUTR",
                "ANPHQIJMXCWOSKTYGULFVERZ",
                "RFYUXJEWCKQOMGATHZVILNSP",
                "SCPYUMQJTVEXKRNLIOWGHAFZ",
                "VIKTSJCEYQGLOMPZWAHFXURN",
                "SVJICLXKHQZTFWNPYRGMEUAO",
                "JRCTHYKIGSXPOZLUQAVNEWFM",
                "NGMSWJITREHFZVQCUKXYAPOL",
                "WUXJOQKGNSYLHEZAFIPMRCVT",
                "PKYQIOLXFCRGHZNAMJVUTWES",
                "FERSGNMJVZXWAYLIKCPUQHTO",
                "HPLRIUQMTSGYJVAXWNOCZEKF",
                "JUVWPTEGCOFYSKXNRMHQALIZ",
                "MWPIAZCNSLEYRTHFKQXUOVGJ",
                "EZXLUNFVCMORSIWKTYHJAQPG",
                "HRQNLTKJFIEGMCSXAZPYOVUW",
                "LOHXVYGWRIJMCPSQENUAKTZF",
                "XKUTWPRGHOAQFLVYMJSNEIZC",
                "WTCRQMVKPHOSLGAXZUEFYNJI",
            ],
            "output": "VWFHSJARNPEMOXLTUKICZGYQ",
        },
    ]
    solution = Solution()

    for param in params:
        n = param["input"]
        result = solution.rankTeams(n)
        print(
            "SUCCESS" if result == param["output"] else "ERROR",
            "input",
            param["input"],
            "output",
            param["output"],
            "result",
            result,
            "\n",
        )


if __name__ == "__main__":
    test()
