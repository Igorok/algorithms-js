import heapq
from collections import Counter, defaultdict
from functools import cache
from json import dumps
from typing import List


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        N = len(s)
        countOfChars = Counter(s)

        stack = []
        visited = {}

        for char in s:
            countOfChars[char] -= 1
            if visited.get(char, 0) > 0:
                continue
                
            while stack and stack[-1] >= char and countOfChars[stack[-1]] > 0:
                prev = stack.pop()
                visited[prev] -= 1

            visited[char] = visited.get(char, 0) + 1
            stack.append(char)

            
        
        return ''.join(stack)
        
        
        
def test():
    params = [
        {
            "input": "bcabc",
            "output": 'abc',
        },
        {
            "input": "cbacdcbc",
            "output": 'acdb',
        },
    ]
    solution = Solution()

    for param in params:
        s = param["input"]
        result = solution.smallestSubsequence(s)
        print(
            "SUCCESS" if result == param["output"] else "ERROR",
            "input",
            param["input"],
            "output",
            param["output"],
            "result",
            result,
            "\n",
        )


if __name__ == "__main__":
    test()
