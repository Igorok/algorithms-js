from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = defaultdict(int)
        for char in s:
            count[char] += 1

        res = []
        start = 0
        visited = defaultdict(int)
        completed = 0
        for i in range(len(s)):
            char = s[i]
            visited[char] += 1
            if visited[char] == count[char]:
                completed += 1

            if completed != 0 and len(visited) == completed:
                res.append(i - start + 1)
                start = i + 1
                completed = 0
                visited = defaultdict(int)


        return res

'''
ababcbaca defegde hijhklij

"ababcbaca", "defegde", "hijhklij".


'''

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
