import json
from collections import deque
from typing import List

class Solution_0:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()

        def dfs(nums):
            if len(nums) == 0:
                return True

            if len(nums) % k != 0:
                return False

            acc = [nums[0]]
            del nums[0]

            i = 0
            while i < len(nums) and len(acc) < k:
                if nums[i] == acc[-1] + 1:
                    acc.append(nums[i])
                    del nums[i]
                else:
                    i += 1

            if len(acc) < k:
                return False

            return dfs(nums)

        return dfs(nums)


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        countOfNums = {}
        for num in nums:
            countOfNums[num] = countOfNums.get(num, 0) + 1

        keys = sorted(countOfNums.keys())


        for key in keys:
            if len(countOfNums) == 0:
                return True

            if not key in countOfNums:
                continue

            _key = key
            cnt = countOfNums[_key]
            _length = 0
            while _length < k:
                if not _key in countOfNums or countOfNums[_key] < cnt:
                    return False

                _length += 1
                if countOfNums[_key] == cnt:
                    del countOfNums[_key]
                else:
                    countOfNums[_key] -= cnt
                _key += 1

        return True




'''
[1,2,3,3,4,4,5,6], 4

1 2 3 4
3 4 5 5


'''

def test():
    params = [
        {
            "input": [[1,2,3,3,4,4,5,6], 4],
            "output": True,
        },
        {
            "input": [[3,2,1,2,3,4,3,4,5,9,10,11], 3],
            "output": True,
        },
        {
            "input": [[1,2,3,4], 3],
            "output": False,
        },
        {
            "input": [[16,21,26,35], 4],
            "output": False,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param["input"]
        result = solution.isPossibleDivide(nums, k)
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
