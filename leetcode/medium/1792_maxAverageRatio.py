from typing import List
from json import dumps
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        res = 0;
        data = []
        for p, t in classes:
            ratio = p/t
            if ratio == 1:
                res += 1
            else:
                key = (p + 1) / (t + 1) - p/t
                data.append((-key, (p, t)))

        heapq.heapify(data)

        while extraStudents > 0 and len(data) > 0:
            key, arr = heapq.heappop(data)
            p, t = arr
            if len(data) == 0:
                heapq.heappush(data, (1, (p + extraStudents, t + extraStudents)))
                extraStudents = 0
                break

            p += 1
            t += 1
            extraStudents -= 1
            key = (p + 1) / (t + 1) - p/t
            heapq.heappush(data, (-key, (p, t)))

        for key, arr in data:
            p, t = arr
            res += (p / t)

        return res / len(classes)

'''
1, 1000
1, 5
1, 2



'''



def test ():
    params = [
        {
            'input': [ [[1,2],[3,5],[2,2]], 2],
            'output': 0.78333,
        },
        {
            'input': [[[2,4],[3,9],[4,5],[2,10]], 4],
            'output': 0.53485,
        },
    ]
    solution = Solution()

    for param in params:
        classes, extraStudents = param['input']
        result = solution.maxAverageRatio(classes, extraStudents)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
