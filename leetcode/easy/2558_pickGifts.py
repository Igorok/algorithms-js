from typing import List
import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        queuePile = [-n for n in gifts]
        heapq.heapify(queuePile)

        print(queuePile)

        for i in range(k):
            if not len(queuePile):
                break

            count = -(heapq.heappop(queuePile))
            sqrt = int(math.isqrt(count))

            if sqrt != 0:
                heapq.heappush(queuePile, -sqrt)

        return sum([-n for n in queuePile])

def test ():
    params = [
        {
            'input': [[25,64,9,4,100], 4],
            'output': 29,
        },
        {
            'input': [[1,1,1,1], 4],
            'output': 4,
        },

    ]
    solution = Solution()

    for param in params:
        gifts, k = param['input']
        result = solution.pickGifts(gifts, k)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
