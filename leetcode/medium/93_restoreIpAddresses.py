from typing import List
import json
from collections import deque, defaultdict
import math

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []

        def dfs(id, step, acc):
            if id == n:
                if step == 4:
                    res.append(acc)
                return

            if step == 4:
                return

            for i in range(1, 4):
                if id + i > n:
                    break

                val = s[id: id + i]
                num = int(val)
                if int(val) > 255:
                    continue
                if val[0] == '0' and len(val) > 1:
                    continue

                upd = val if id == 0 else acc+'.'+val
                dfs(id + i, step+1, upd)

        dfs(0, 0, '')

        return res


def test ():
    params = [
        {
            'input': "010010",
            'output': ["0.10.0.10","0.100.1.0"],
        },
        {
            'input': "25525511135",
            'output': ["255.255.11.135","255.255.111.35"],
        },
        {
            'input': "0000",
            'output': ["0.0.0.0"],
        },
        {
            'input': "101023",
            'output': ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"],
        },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.restoreIpAddresses(s)
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
