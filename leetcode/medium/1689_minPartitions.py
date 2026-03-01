from typing import List
from json import dumps
from collections import deque

class Solution_0:
    def minPartitions(self, n: str) -> int:
        res = 0
        while n != '':
            upd = ''
            for char in n:
                num = int(char)
                if num != 0:
                    num -= 1
                if num == 0 and upd == '':
                    continue
                else:
                    upd += str(num)
            n = upd
            res += 1

        return res


class Solution_1:
    def minPartitions(self, n: str) -> int:
        num = deque([int(v) for v in n])

        res = 0
        while num:
            res += 1
            for i in range(len(num)):
                if num[i] >= 1:
                    num[i] -= 1
            while num and num[0] == 0:
                num.popleft()

        return res

class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))


'''

320
110

210
110

100
000

---

82734
11111

71623
11111

60512
10111

50501


---

3005
1001

2004
1001

1003
1001

0002
2
1

1
1

---

3005
1111

11
19







'''



def test ():
    params = [
        {
            'input': "320", # 110 + 110 + 100
            'output': 3,
        },
        {
            'input': "32",
            'output': 3,
        },
        {
            'input': "82734",
            'output': 8,
        },
        {
            'input': "27346209830709182346",
            'output': 9,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.minPartitions(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
