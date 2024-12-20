from typing import List
from json import dumps
import heapq

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        charsFreq = {}
        for i in range(len(s)):
            freq = charsFreq.get(s[i], 0)
            charsFreq[s[i]] = freq + 1

        chars = [-ord(k) for k in charsFreq]
        heapq.heapify(chars)
        res = ''

        while chars:
            i = -heapq.heappop(chars)
            char = chr(i)
            if len(res) != 0 and char == res[-1]:
                if len(chars) == 0:
                    break
                else:
                    prevI = i
                    i = -heapq.heappop(chars)
                    char = chr(i)
                    heapq.heappush(chars, -prevI)
                    charsFreq[char] -= 1
                    res += char
            else:
                freq = min(charsFreq[char], repeatLimit)
                charsFreq[char] = max(charsFreq[char] - repeatLimit, 0)
                res += char*freq

            if charsFreq[char] > 0:
                heapq.heappush(chars, -i)


        return res

def test ():
    params = [
        {
            'input': ['cczazcc', 3],
            'output': 'zzcccac',
        },
        {
            'input': ['aababab', 2],
            'output': 'bbabaa',
        },
    ]
    solution = Solution()

    for param in params:
        s, repeatLimit = param['input']
        result = solution.repeatLimitedString(s, repeatLimit)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
