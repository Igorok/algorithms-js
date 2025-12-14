from typing import List
from collections import deque
from functools import cache
import re


class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        cLen = len(code)
        bLen = len(businessLine)
        aLen = len(isActive)

        memo = {
            "electronics": [], "grocery": [], "pharmacy": [], "restaurant": []
        }

        for i in range(cLen):
            if i == bLen  or i == aLen:
                break

            if not isActive[i]:
                continue
            if businessLine[i] not in memo:
                continue
            if not code[i]:
                continue
            matches = re.findall(r'\W', code[i])
            if len(matches):
                continue

            memo[businessLine[i]].append(code[i])


        res = []
        for key in memo:
            memo[key].sort()
            res = res + memo[key]

        return res



def test ():
    params = [
        {
            'input': [
                ["SAVE20","","PHARMA5","SAVE@20"], ["restaurant","grocery","pharmacy","restaurant"], [True,True,True,True]
            ],
            'output': ["PHARMA5","SAVE20"],
        },
        {
            'input': [
                ["GROCERY15","ELECTRONICS_50","DISCOUNT10"], ["grocery","electronics","invalid"], [False,True,True]
            ],
            'output': ["ELECTRONICS_50"],
        },
    ]
    solution = Solution()

    for param in params:
        code, businessLine, isActive = param['input']
        result = solution.validateCoupons(code, businessLine, isActive)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            # 'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
