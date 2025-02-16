from typing import List
from json import dumps
import heapq
from collections import deque, defaultdict

class Solution:
    def constructDistancedSequence_0(self, n: int) -> List[int]:
        used = [None] * (n+1)
        length = (n-1)*2 + 1
        arr = [None] * length
        completed = None

        def rec():
            nonlocal used, arr, length, n, completed
            if completed:
                return

            visited = 0
            for i in range(length):
                if arr[i]:
                    visited += 1
                    continue
                for num in range(n, 0, -1):
                    if used[num]:
                        visited += 1
                        continue
                    if num == 1:
                        used[num] = True
                        arr[i] = num
                        rec()
                        used[num] = None
                        arr[i] = None
                    elif num > 1 and i+num < length and not arr[i+num]:
                        used[num] = True
                        arr[i] = arr[i+num] = num
                        rec()
                        used[num] = None
                        arr[i] = arr[i+num] = None


            if visited == length and not completed:
                completed = arr.copy()

        rec()

        return completed


    def constructDistancedSequence(self, n: int) -> List[int]:
        length = (n-1)*2 + 1
        arr = [None] * length
        used = [None]*(n+1)

        def rec(id):
            nonlocal arr, length

            if id == length:
                return True

            if arr[id]:
                return rec(id+1)

            for num in range(n, 0, -1):
                if used[num]:
                    continue

                if num == 1:
                    arr[id] = num
                    used[num] = True
                    if rec(id+1):
                        return True
                    arr[id] = None
                    used[num] = None
                elif id + num < length and not arr[id + num]:
                    arr[id] = arr[id + num] = num
                    used[num] = True
                    if rec(id+1):
                        return True
                    arr[id] = arr[id + num] = None
                    used[num] = None

            return False

        rec(0)

        return arr


'''

[16,14,15,11,9,13,6,4,12,10,1,4,6,9,11,14,16,15,13,10,12,8,5,7,2,3,2,5,3,8,7]
[16,14,15,11,9,13,6,4,1,12,10,4,6,9,11,14,16,15,13,8,10,12,3,7,5,3,2,8,2,5,7]

'''

def test ():
    params = [
        {
            'input': 3,
            'output': [3,1,2,3,2],
        },
        {
            'input': 5,
            'output': [5,3,1,4,3,5,2,4,2],
        },
        {
            'input': 16,
            'output': [16,14,15,11,9,13,6,4,12,10,1,4,6,9,11,14,16,15,13,10,12,8,5,7,2,3,2,5,3,8,7],
        },
        {
            'input': 10,
            'output': [10, 8, 6, 9, 3, 1, 7, 3, 6, 8, 10, 5, 9, 7, 4, 2, 5, 2, 4],
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.constructDistancedSequence(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
