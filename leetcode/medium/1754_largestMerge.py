from typing import List
import json
from collections import deque, defaultdict


class Solution_0:
    def largestMerge(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)

        res = []

        i = 0
        j = 0

        while i < n and j < m:
            if word1[i] >= word2[j]:
                res.append(word1[i])
                i += 1
            else:
                res.append(word2[j])
                j += 1

        for i1 in range(i, n):
            res.append(word1[i1])
        for j1 in range(j, m):
            res.append(word2[j1])

        return ''.join(res)


class Solution_1:
    def largestMerge(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)

        res = ''

        i = 0
        j = 0
        while len(res) < (n+m):
            diff = 0
            while i + diff < n and j + diff < m and word1[i + diff] == word2[j + diff]:
                diff += 1

            if i + diff < n and j + diff == m:
                res += word1[i : i+diff+1]
                i += diff+1
                continue

            if j + diff < m and i + diff == n:
                res += word2[j : j + diff+1]
                j += diff+1
                continue

            if i + diff == n and j + diff == m:
                res += word1[i : i+diff+1]
                i += diff+1
                continue

            if word1[i+diff] >= word2[j+diff]:
                res += word1[i : i+diff+1]
                i += diff+1
            else:
                res += word2[j : j + diff+1]
                j += diff+1

        return res

class Solution_2:
    def largestMerge(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)

        res = ''

        i = 0
        j = 0
        while len(res) < (n+m):
            diff = 0
            while i + diff < n and j + diff < m and word1[i + diff] == word2[j + diff]:
                diff += 1

            selected = 2
            if (i + diff < n and j + diff == m) or (i + diff == n and j + diff == m) or (i + diff < n and word1[i + diff] >= word2[j + diff]):
                selected = 1

            if selected == 1:
                end = min(n, i + diff + 1)
                while i < end:
                    if j == m or word1[i] >= word2[j]:
                        res += word1[i]
                        i += 1
                    else:
                        res += word2[j]
                        j += 1
            else:
                end = min(m, j + diff + 1)
                while j < end:
                    if i == n or word2[j] >= word1[i]:
                        res += word2[j]
                        j += 1
                    else:
                        res += word1[i]
                        i += 1

        return res

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)

        res = ''

        i = 0
        j = 0
        while i < n and j < m:
            if word1[i:] > word2[j:]:
                res += word1[i]
                i += 1
            else:
                res += word2[j]
                j += 1

        res += word1[i:] + word2[j:]

        return res

'''
abcabc
abdcaba
abdcabcabcaba
abcabcabdcaba

---

abbc
abbd

abbcabbd

---

abc
bbc

---

abc
abcd

---

input ["uuurruuuruuuuuuuuruuuuu", "urrrurrrrrrrruurrrurrrurrrrruu"]
output "uuuurruuuruuuuuuuuruuuuurrrurrrrrrrruurrrurrrurrrrruu"
result "uuurruuuuruuuuuuuuruuuuurrrurrrrrrrruurrrurrrurrrrruu"

uuurruuuruuuuuuuuruuuuu
urrrurrrrrrrruurrrurrrurrrrruu
uuurruuuuruuuuuuuuruuuuurrrurrrrrrrruurrrurrrurrrrruu


urruuuruuuuuuuuruuuuu
urrrurrrrrrrruurrrurrrurrrrruu

uu

'''


def test ():
    params = [
        {
            'input': ["uuurruuuruuuuuuuuruuuuu", "urrrurrrrrrrruurrrurrrurrrrruu"],
            'output': 'uuuurruuuruuuuuuuuruuuuurrrurrrrrrrruurrrurrrurrrrruu',
        },
        {
            'input': ["cabaa", "bcaaa"],
            'output': 'cbcabaaaaa',
        },
        {
            'input': ["abcabc", "abdcaba"],
            'output': 'abdcabcabcaba',
        },
    ]
    solution = Solution()

    for param in params:
        word1, word2 = param['input']
        result = solution.largestMerge(word1, word2)
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
