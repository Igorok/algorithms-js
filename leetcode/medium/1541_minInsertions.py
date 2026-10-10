import json
from collections import defaultdict, deque
from functools import cache
from typing import List

"""

) (
) = ( )
( = ) )
4

) ( )
) = ( )
( = )
3

) ( ) ( ) ) ) )


"""


class Solution_0:
    def minInsertions(self, s: str) -> int:
        N = len(s)
        res = 0

        open = deque()
        closed = []

        def popClosed():
            nonlocal res

            while len(closed) >= 2:
                if len(open) > 0 and open[0] < closed[-2]:
                    open.popleft()
                    closed.pop()
                    closed.pop()
                else:
                    closed.pop()
                    closed.pop()
                    res += 1

        for i in range(N):
            char = s[i]
            if char == "(":
                open.append(i)
            else:
                closed.append(i)

            popClosed()

        if (len(closed) % 2) == 1:
            closed.append(N + 1)
            res += 1

        popClosed()
        if len(open):
            res += len(open) * 2

        return res


"""

Do you know the issue - 1541. Minimum Insertions to Balance a Parentheses String?

I waste more than hour and solve the issue 2 times, but my solution is wrong:

Here:
Input: s = "(()))"
Output: 1

Because we just should use 2 closed braces.

Here:
Input: s =  "(()))(()))()())))",
Output: 4,

Because we can not just use a 2 closed braces, they must be consecutive

How to understand description:
    (***)) - consecutive?
    (*)*) - not consecutive?


(()))(()))()())))
(()))(()))()())))


(()))(()))()())))
()()()())


()()()()()(
()()()()()(
2
()()()()()
3
()()()()


"""


class Solution:
    def minInsertions(self, s: str) -> int:
        N = len(s)
        res = 0

        open = []
        closed = []

        for i in range(N):
            char = s[i]
            if char == "(":
                open.append(i)
            else:
                closed.append(i)

            if len(closed) > 1 and closed[-2] + 1 == closed[-1]:
                if len(open) > 0:
                    open.pop()
                else:
                    res += 1
                closed.pop()
                closed.pop()

        # print("open", open, "closed", closed)

        while len(open):
            i = open.pop()
            if len(closed) and closed[-1] > i:
                res += 1
                closed.pop()
            else:
                res += 2

        if len(closed):
            res += len(closed) * 2

        return res


def test():
    params = [
        {
            "input": "(()))",
            "output": 1,
        },
        {
            "input": "())",
            "output": 0,
        },
        {
            "input": "))())(",
            "output": 3,
        },
        {
            "input": "(()))(()))()())))",
            "output": 4,
        },
        {
            "input": "()()()()()(",
            "output": 7,
        },
    ]
    solution = Solution()

    for param in params:
        s = param["input"]
        result = solution.minInsertions(s)
        correct = json.dumps(result) == json.dumps(param["output"])

        msg = "SUCCESS" if correct else "ERROR"
        msg += "\n"
        if not correct:
            msg += "input " + json.dumps(param["input"]) + "\n"
            msg += "output " + json.dumps(param["output"]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

        print(msg)


if __name__ == "__main__":
    test()
