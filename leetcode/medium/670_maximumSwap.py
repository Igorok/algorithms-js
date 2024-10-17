from typing import List
import math

class Solution:
    def maximumSwap(self, num: int) -> int:
        data = list(str(num))
        dataSorted = [(data[i], i) for i in range(len(data))]
        dataSorted = sorted(dataSorted, key=lambda x: -int(x[0]))

        print(
            'data', data,
            'dataSorted', dataSorted,
        )

        toReplaceId = None
        maxNum = None
        for i in range(len(data)):
            v = data[i]
            vs = dataSorted[i][0]
            ids = dataSorted[i][1]
            if v != vs and ids > i and toReplaceId == None:
                toReplaceId = i
                maxNum = dataSorted[i]
            if maxNum != None and dataSorted[i][0] >= maxNum[0]:
                maxNum = dataSorted[i]

        if toReplaceId != None:
            data[toReplaceId], data[maxNum[1]] = data[maxNum[1]], data[toReplaceId]
            return int(''.join(data))


        return num


def test ():
    params = [
        {
            'input': 2736,
            'output': 7236,
        },
        {
            'input': 9973,
            'output': 9973,
        },
        {
            'input': 985438,
            'output': 988435,
        },
        {
            'input': 1993,
            'output': 9913,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.maximumSwap(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
