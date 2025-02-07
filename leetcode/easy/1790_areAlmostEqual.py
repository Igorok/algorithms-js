from typing import List
import json
from collections import deque

class Solution:
    def areAlmostEqual_0(self, s1: str, s2: str) -> bool:
        arr1 = list(s1)
        arr1.sort()
        arr2 = list(s2)
        arr2.sort()
        return arr1 == arr2


    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        splited = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                splited.append(i)
                if len(splited) > 2:
                    return False


        if len(splited) == 0:
            return True


        return len(splited) == 2 and s1[splited[0]] == s2[splited[1]] and s1[splited[1]] == s2[splited[0]]


def test ():
    params = [
        {
            'input': ["bank", "kanb"],
            'output': True,
        },
        {
            'input': ["attack", "defend"],
            'output': False,
        },
        {
            'input': ["kelb", "kelb"],
            'output': True,
        },
        {
            'input': ["abcd", "dcba"],
            'output': False,
        },
    ]
    solution = Solution()

    for param in params:
        s1, s2 = param['input']
        result = solution.areAlmostEqual(s1, s2)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
