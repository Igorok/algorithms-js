from typing import List
import json

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for char in s:
            c = count.get(char, 0)
            count[char] = c + 1

        for i in range(len(s)):
            char = s[i]
            if count[char] == 1:
                return i

        return -1



def test ():
    params = [
        {
            'input': "leetcode",
            'output': 0,
        },
        {
            'input': "loveleetcode",
            'output': 2,
        },
        {
            'input': "aabb",
            'output': -1,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.firstUniqChar(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
