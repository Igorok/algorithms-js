from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chars = defaultdict(int)
        for i in range(len(s)):
            char = s[i]
            chars[char] = i

        res = []
        subChars = set()
        lastChars = 0
        length = 0
        for i in range(len(s)):
            length += 1
            char = s[i]
            subChars.add(char)
            if chars[char] == i:
                lastChars += 1
                if lastChars == len(subChars):
                    res.append(length)
                    subChars = set()
                    lastChars = 0
                    length = 0

        if length:
            res.append(length)

        return res


def test ():
    params = [
        {
            'input': 'ababcbacadefegdehijhklij',
            'output': [9,7,8],
        },
        {
            'input': 'eccbbbbdec',
            'output': [10],
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.partitionLabels(nums)
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
