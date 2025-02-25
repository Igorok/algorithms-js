from typing import List
import json
from collections import deque, defaultdict
import heapq

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        def isEqualMaps(correct, target):
            for k in correct:
                if correct[k] != target[k]:
                    return False
            return True

        lengthP = len(p)
        countP = 0
        charsP = defaultdict(int)
        for char in p:
            countP += 1
            charsP[char] += 1

        countS = 0
        charsS = defaultdict(int)
        for i in range(lengthP):
            char = s[i]
            if char in charsP:
                countS += 1
                charsS[char] += 1

        res = []
        if countS == countP and isEqualMaps(charsP, charsS):
            res.append(0)

        for i in range(1, len(s) - lengthP + 1):
            prev = s[i-1]
            char = s[i+lengthP-1]

            charsS[char] += 1
            charsS[prev] -= 1
            if charsS[prev] == 0:
                charsS.pop(prev)
            if prev in charsP:
                countS -= 1
            if char in charsP:
                countS += 1

            if countS == countP and isEqualMaps(charsP, charsS):
                res.append(i)

        return res


def test ():
    params = [
        {
            'input': ["aaaaaaaaaa", "aaaaaaaaaaaaa"],
            'output': [],
        },
        {
            'input': ["cbaebabacd", "abc"],
            'output': [0,6],
        },
        {
            'input': ["abab", "ab"],
            'output': [0,1,2],
        },
    ]
    solution = Solution()

    for param in params:
        s, p = param['input']
        result = solution.findAnagrams(s, p)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
