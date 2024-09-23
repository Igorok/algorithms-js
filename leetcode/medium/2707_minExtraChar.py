from typing import List
from collections import defaultdict

# 2707. Extra Characters in a String
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        cache = {}
        words = set(dictionary)

        used = 0
        def rec(start):
            if start in cache:
                return cache[start]

            if start >= len(s):
                return 0

            u = rec(start + 1)
            use = 0

            for word in words:
                l = len(word)
                if start + l <= len(s) and s[start : start + l] == word:
                    r = rec(start + l)
                    use = max(use, l + r)

            cache[start] = max(u, use)
            return cache[start]

        used = rec(0)

        return len(s) - used


'''

"leet","code","leetcode"
leetscode
leet - 4
scode - 0
code - 4
9 - 8 = 1

sayhelloworld
sayhelloworld - 13
ayhelloworld - 12 + 1
yhelloworld - 11 + 1 + 1
helloworld - 10 + 1 + 1 + 1
hello/world - 10 + 1 + 1 + 1 - 5 = 5 + 3 = 8
world/ - 8 - 5 = 3


'''


def test ():
    params = [
        {
            'input': ["leetscode", ["leet","code","leetcode"]],
            'output': 1,
        },
        {
            'input': ["sayhelloworld", ["hello","world"]],
            'output': 3,
        },
        {
            'input': ["dwmodizxvvbosxxw", ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]],
            'output': 7,
        },
        {
            'input': ["smsvy", ["j","p","y","r","t","nj","k","xj","vg","da","m","u","yq","as","wh","b","vo","h","wb","z","np","uy","i","f","w","wg","s","ls","xf","ou","mj","pf"]],
            'output': 1,
        },
    ]
    solution = Solution()

    for param in params:
        s, dictionary = param['input']

        result = solution.minExtraChar(s, dictionary)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
