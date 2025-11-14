import json
from collections import deque
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        unique = set()

        def dfs(id, acc):
            if len(acc) >= 2:
                tpl = tuple(acc)
                if tpl in unique:
                    return
                unique.add(tpl)

            if id == n:
                return

            if not acc or acc[-1] <= nums[id]:
                _acc = acc.copy()
                _acc.append(nums[id])
                dfs(id+1, _acc)

            _acc = acc.copy()
            dfs(id+1, _acc)

            return

        dfs(0, [])

        return list(unique)


def test():
    params = [
        {
            "input": [4, 6, 7, 7],
            "output": [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]],
        },
        {
            "input": [4,4,3,2,1],
            "output": [[4,4]],
        },
    ]
    solution = Solution()

    for param in params:
        nums = param["input"]
        result = solution.findSubsequences(nums)
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
