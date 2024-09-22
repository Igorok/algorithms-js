from typing import List

class Solution:
    def findKthNumber_slow(self, n: int, k: int) -> int:
        arr = []

        def rec(start):
            if start > n or len(arr) > k:
                return
            arr.append(start)
            fc = start * 10
            lc = (start + 1) * 10
            for i in range(fc, lc):
                if i > n or len(arr) > k:
                    break
                rec(i)


        for i in range(1, 10):
            rec(i)

        # print('arr', arr)

        return arr[k - 1]

    def findKthNumber(self, n: int, k: int) -> int:
        pos = 1
        start = 1

        def getSteps(s, e):
            steps = 0
            while s <= n:
                steps += min(e, n + 1) - s
                s *= 10
                e *= 10
            return steps


        while pos < k:
            steps = getSteps(start, start + 1)
            print(
                'start', start,
                'steps', steps,
            )
            if pos + steps <= k:
                pos += steps
                start += 1
            else:
                pos += 1
                start *= 10


        return start


'''

                0
        1                                                           2       3       ...         9
10      11      12      13      ..      19
100
1000

'''


def test ():
    params = [
        {
            'input': [13, 2],
            'output': 10,
        },
        {
            'input': [100, 90],
            'output': 9,
        },
        {
            'input': [1, 1],
            'output': 1,
        },
        {
            'input': [6516650, 3611122],
            'output': 4250005,
        },
        {
            'input': [5202363, 3078011],
            'output': 3770206,
        },
    ]
    solution = Solution()

    for param in params:
        n, k = param['input']
        result = solution.findKthNumber(n, k)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()

