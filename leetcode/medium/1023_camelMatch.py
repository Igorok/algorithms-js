import heapq
import json
from collections import defaultdict, deque
from functools import cache
from typing import List

'''
class Cat:
    def __init__(self, name):
        self.__name = name

c = Cat("qwe")

print(c.__dir__())
print(c._Cat__name)
c._Cat__name = "new qwe"
print(c._Cat__name)
'''



class Solution:
    def camelMatch(self, queries: list[str], pattern: str) -> list[bool]:
        N = len(pattern)
        def checkPattern(word):
            M = len(word)
            id = 0
            for i in range(M):
                if word[i].upper() == word[i]:
                    if id == N:
                        return False

                    if word[i] == pattern[id]:
                        id += 1
                    else:
                        return False
                else:
                    if id == N:
                        continue

                    if word[i] == pattern[id]:
                        id += 1
                        continue


            return id == N


        return [checkPattern(w) for w in queries]

def test():
    params = [
        {
            "input": [["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB"],
            "output": [True,False,True,True,False],
        },

        {
            "input": [["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBa"],
            "output": [True,False,True,False,False],
        },

        {
            "input": [["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBaT"],
            "output": [False,True,False,False,False],
        },
    ]
    solution = Solution()

    for param in params:
        queries, pattern = param["input"]
        result = solution.camelMatch(queries, pattern)
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
