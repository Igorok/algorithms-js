from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def partition_0(self, s: str) -> List[List[str]]:
        res = set()
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                text = s[i: j+1]
                text2 = list(text)
                text2.reverse()
                text2 = ''.join(text2)
                if text == text2:
                    res.add(text)

        return list(res)


    def partition(self, s: str) -> List[List[str]]:
        def isPalindrom(text):
            start = 0
            end = len(text)-1
            while start < end:
                if text[start] != text[end]:
                    return False
                start += 1
                end -= 1

            return True

        res = []

        def rec(text, arr):
            if not text and arr:
                res.append(arr.copy())

            for i in range(1, len(text)+1):
                t = text[:i]
                if isPalindrom(t):
                    a = arr.copy()
                    a.append(t)
                    rec(text[i:], a)

        rec(s, [])

        return res

'''

aaaaaaa
abcdeee



'''

def test ():
    params = [
        {
            'input': 'aab',
            'output': [["a","a","b"],["aa","b"]],
        },
        {
            'input': 'a',
            'output': [["a"]],
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.partition(nums)
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
