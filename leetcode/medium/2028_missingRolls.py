from typing import List
import json
import math


class Solution:
    def check(self, rolls, mean):
        s = sum(rolls)
        m = s / len(rolls)
        print('check', m, mean)

    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        mSum = sum(rolls)
        length = len(rolls) + n
        # rollSum / length = mean
        # rollSum = length * mean
        rollSum = length * mean
        nSum = rollSum - mSum

        print('nSum', nSum)

        if math.ceil(nSum / n) > 6:
            return []
        if nSum // n < 1:
            return []

        avr = nSum // n
        rem = nSum % n
        result = [0] * n
        for i in range(n):
            if i == n - 1:
                result[i] = nSum
            else:
                result[i] = avr
                nSum -= avr
                if rem != 0:
                    result[i] += 1
                    rem -= 1
                    nSum -= 1


        print('nSum', nSum)


        self.check(rolls + result, mean)

        return result




def test ():
    params = [
        {
            'input': [[3,2,4,3], 4, 2],
            'output': [6,6],
        },
        {
            'input': [[1,5,6], 3, 4],
            'output': [2,3,2,2],
        },
        {
            'input': [[1,2,3,4], 6, 4],
            'output': [],
        },

        {
            'input': [[4,5,6,2,3,6,5,4,6,4,5,1,6,3,1,4,5,5,3,2,3,5,3,2,1,5,4,3,5,1,5], 4, 40],
            'output': [4,4,4,4,4,4,5,5,4,4,4,5,4,4,4,4,4,4,4,4,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5],
        },

    ]
    solution = Solution()

    for param in params:
        rolls, mean, n = param['input']
        result = solution.missingRolls(rolls, mean, n)
        print(
            'SUCCESS' if json.dumps(sorted(result)) == json.dumps(sorted(param['output'])) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
