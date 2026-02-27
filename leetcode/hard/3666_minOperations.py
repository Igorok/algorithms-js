from typing import List
import json
from collections import deque, defaultdict
import heapq
import bisect

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        target = 0
        initial_zeros = s.count('0')

        if initial_zeros == 0:
            return 0

        unvisited = [[],[]]
        for i in range(n+1):
            if i != initial_zeros:
                unvisited[i % 2].append(i)

        queue = deque([(initial_zeros, 0)])

        while queue:
            cur, dist = queue.popleft()

            max_x = min(cur, k)
            # notTakenFlip = k - max_x
            L = cur - max_x + k - max_x

            # v = n - cur count of 1
            # k -v - max count of 1 which we can flip
            min_x = max(0, k - (n - cur))

            # ?
            R = cur + k - 2 * min_x

            parity = L % 2
            curr_unvisited = unvisited[parity]

            idx_start = bisect.bisect_left(curr_unvisited, L)
            idx_end = bisect.bisect_right(curr_unvisited, R)


            to_visit = curr_unvisited[idx_start:idx_end]

            for val in to_visit:
                if val == target:
                    return dist + 1
                queue.append((val, dist + 1))

            del curr_unvisited[idx_start:idx_end]

        return -1


'''

101
011
000
110


'''


def test ():
    params = [
        {
            'input': ["110", 1],
            'output': 1,
        },
        {
            'input': ["0101", 3],
            'output': 2,
        },
        {
            'input': ["101", 2],
            'output': -1,
        },
    ]
    solution = Solution()

    for param in params:
        s, k = param['input']
        result = solution.minOperations(s, k)
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
