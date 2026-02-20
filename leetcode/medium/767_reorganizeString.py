from typing import List
import json
from collections import deque, defaultdict
import heapq



class Solution_0:
    def reorganizeString(self, s: str) -> str:
        chars = {}
        for char in s:
            chars[char] = chars.get(char, 0) + 1

        arr = [(v, k) for k, v in chars.items()]
        arr.sort(key = lambda x: x[0], reverse = True)
        arr = deque(arr)

        res = ''
        while arr:
            v, char = arr.popleft()
            if res and res[-1] == char:
                return ''

            res += char
            v -= 1
            if v > 0:
                arr.append((v, char))

        return res

class Solution:
    def reorganizeString(self, s: str) -> str:
        chars = {}
        for char in s:
            chars[char] = chars.get(char, 0) + 1

        arr = [(-v, k) for k, v in chars.items()]
        heapq.heapify(arr)

        res = ''
        while arr:
            cnt1, char1 = heapq.heappop(arr)
            if res and res[-1] == char1:
                return ''

            res += char1
            cnt1 += 1

            if arr:
                cnt2, char2 = heapq.heappop(arr)
                res += char2
                cnt2 += 1
                if cnt2 < 0:
                    heapq.heappush(arr, (cnt2, char2))

            if cnt1 < 0:
                heapq.heappush(arr, (cnt1, char1))


        return res

'''

l

'''

def test ():
    params = [
        {
            'input': 'aab',
            'output': 'aba',
        },
        {
            'input': 'aaab',
            'output': '',
        },
        {
            'input': 'vvvlo',
            'output': 'vlvov',
        },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.reorganizeString(s)
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
