from typing import List
import json
from collections import deque, defaultdict
import heapq


class Solution:
    def checkValidString(self, s: str) -> bool:
        N = len(s)
        opens = []
        stars = []

        for i in range(N):
            if s[i] == '*':
                stars.append(i)
            if s[i] == '(':
                opens.append(i)
            if s[i] == ')':
                if opens:
                    opens.pop()
                    continue
                if stars:
                    stars.pop()
                    continue

                return False


        while opens and stars:
            if stars[-1] > opens[-1]:
                opens.pop()
                stars.pop()
            else:
                break

        return len(opens) == 0


def test ():
    params = [
        {
            'input': "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()",
            'output': True,
        },
        {
            'input': "***((()",
            'output': False,
        },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.checkValidString(s)
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
