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

            # how many zeros we have
            max_x = min(cur, k)
            # I will flip all zeros, but may be I have not enough zeros and I must take a ones
            # countOfZeros = min(curr, k)
            # countOfOnes = k - countOfZeros
            # resultOfFlip = cur - countOfZeros + countOfOnes = cur - max_x + k - max_x
            L = cur + k - 2 * max_x

            # how many zeros we must take?
            # countOfOnes = n - cur
            # countOfZeros = max(0, k - (n - cur))
            min_x = max(0, k - (n - cur))
            # resultOfFlip = cur - countOfZeros + countOfOnes = cur - min_x + k - min_x = cur + k -2 * min_x
            R = cur + k - 2 * min_x

            # 2 * min_x
            # count of selected zeros always even
            # so if we had odd zeros, after flip we will have only odd zeros
            # if we had even zeros, after flip, we will have only even zeros
            # should use only even or odd part of unvisited values
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

0-7
1-3
k=4

4+0
7-4, 3+4 = 3, 7

3+1
7-3+1, 3-1+3 = 5, 5

2+2
7-2+2, 3-2+2 = 7, 3

1, 3
7-1+3, 3-3+1 = 9, 1




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
