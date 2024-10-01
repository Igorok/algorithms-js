import time
from typing import List


class Solution_:
    def canArrange(self, arr: List[int], k: int) -> bool:
        s = 0
        remainders = {}
        for i in range(len(arr)):
            r = arr[i] % k
            if not r in remainders:
                remainders[r] = 0
            remainders[r] += 1
            s += r

        if s % k != 0:
            return False

        for key in remainders:
            count = remainders[key]
            if key == 0:
                if count % 2 != 0:
                    return False
                else:
                    continue

            nextKey = k - key
            nextCount = remainders.get(nextKey, 0)
            if count != nextCount:
                return False

        return True


def test ():
    params = [
        {
            'input': [[1,2,3,4,5,10,6,7,8,9], 5],
            'output': True,
        },
        {
            'input': [[1,2,3,4,5,6], 7],
            'output': True,
        },
        {
            'input': [[1,2,3,4,5,6], 10],
            'output': False,
        },
        {
            'input': [[-10,10], 2],
            'output': True,
        },
    ]

    for param in params:
        start_time = time.time()

        arr, k = param['input']
        solution = Solution()
        result = solution.canArrange(arr, k)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            'time', time.time() - start_time,
            '\n',
        )

if __name__ == '__main__':
    test()
