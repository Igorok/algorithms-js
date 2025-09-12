from typing import List
import json


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 7 + 10**9
        newCount = [0]*(n+1)
        newCount[1] = 1
        waitingCount = [0]*(n+1)
        waitingCount[0] = 1
        waitingCount[1] = 1
        activeCount = [0]*(n+1)



        for day in range(1, n+1):
            activate = 0 if day - delay <= 0 else newCount[day-delay]
            deactivate = 0 if day - forget <= 0 else newCount[day-forget]

            waitingCount[day] = waitingCount[day-1] - activate
            activeCount[day] = activeCount[day-1] - deactivate + activate

            newCount[day] = (newCount[day] + activeCount[day]) % mod
            waitingCount[day] = (waitingCount[day] + activeCount[day]) % mod


        return (activeCount[n] + waitingCount[n]) % mod

'''

wait - ?
activate - ?

active - ?
sharing - ?



'''


def test ():
    params = [
        {
            'input': [6, 2, 4],
            'output': 5,
        },
        {
            'input': [4, 1, 3],
            'output': 6,
        },
    ]
    solution = Solution()

    for param in params:
        n, delay, forget = param['input']
        result = solution.peopleAwareOfSecret(n, delay, forget)
        print(
            'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
