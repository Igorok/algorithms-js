from typing import List
import heapq
import math
from collections import defaultdict, deque

class Solution_0:
    def makeLargestSpecial(self, s: str) -> str:
        N = len(s)

        visited = {}
        visited[s] = s

        def dfs(s):
            res = s

            for l1 in range(N-4):
                z = 0
                o = 0
                pOk = True
                sOk = True
                for r1 in range(l1, N-2):
                    z += 1 if s[r1] == '0' else 0
                    o += 1 if s[r1] == '1' else 0
                    pOk = o >= z
                    sOk = z == o

                    if not pOk:
                        break

                    if sOk:
                        z2 = 0
                        o2 = 0
                        pOk2 = True
                        sOk2 = True

                        for r2 in range(r1+1, N):
                            z2 += 1 if s[r2] == '0' else 0
                            o2 += 1 if s[r2] == '1' else 0
                            pOk2 = o2 >= z2
                            sOk2 = z2 == o2

                            if not pOk2:
                                break

                            if sOk2:
                                s1 = s[:l1]
                                s2 = s[l1:r1+1]
                                s3 = s[r1+1: r2+1]
                                s4 = s[r2+1:]

                                r = s1 + s3 + s2 + s4

                                if r not in visited and r > s:
                                    visited[r] = r
                                    r = dfs(r)

                                if r > res:
                                    res = r

            visited[s] = res
            return res


        return dfs(s)

class Solution:
    def makeLargestSpecial(self, s: str) -> str:

        def dfs(s):
            left = 0
            cnt = 0
            acc = []

            for right in range(len(s)):
                cnt += 1 if s[right] == '1' else -1

                # special string
                if cnt == 0:
                    s1 = '1' + dfs(s[left+1: right]) + '0'
                    acc.append(s1)
                    left = right + 1

            acc.sort(reverse=True)
            return ''.join(acc)

        return dfs(s)

'''
11011000
1 10 1100 0
1 10 1100 0

---

1100 1100 10 1100 110100 10 11110000 1100 111110100000 10

---
111110100000111100001101001100110011001100101010


---

1100101100
1100 10 1100


'''


def test ():
    params = [
        {
            'input': '11011000',
            'output': '11100100',
        },
        {
            'input': '10',
            'output': '10',
        },
        {
            'input': '110011001011001101001011110000110011111010000010',
            'output': '111110100000111100001101001100110011001100101010',
        },
        {
            'input': '1100101100',
            'output': '1100110010',
        },
        # {
        #     'input': '110011001011001101001011110000110011111010000010101',
        #     'output': '111110100000111100001101001100110011001100101010101',
        # },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.makeLargestSpecial(s)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
