import json
from collections import defaultdict, deque
from typing import List
# from functools import cache
import math
import heapq

class Solution_0:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0

        prev = nums[0]
        curr = prev
        for i in range(1, N):
            if curr >= prev:
                prev = curr
                curr = nums[i]
                continue

            curr += nums[i]
            res += 1

        if curr < prev:
            res += 1
            curr += prev



        return res

class Node:
    id = 1
    val = 0
    left = None
    right = None

    def __init__(self, id, val, left, right):
        self.id = id
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if not other:
            return False
        return self.id == other.id

    def __lt__(self, other):
        if not other:
            return False
        return self.id < other.id

    def __gt__(self, other):
        if not other:
            return False
        return self.id > other.id

    def __le__(self, other):
        if not other:
            return False
        return self.id <= other.id

    def __ge__(self, other):
        if not other:
            return False
        return self.id >= other.id

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        N = len(nums)

        sumQueue = []
        violations = 0
        nodes = [Node(i, nums[i], None, None) for i in range(N)]

        for i in range(N):
            if i > 0:
                nodes[i].left = nodes[i-1]
                if nodes[i-1].val > nodes[i].val:
                    violations += 1
                sumQueue.append((
                    nodes[i-1].val + nodes[i].val,
                    nodes[i-1].id,
                    nodes[i-1],
                    nodes[i]
                ))
            if i < N-1:
                nodes[i].right = nodes[i+1]

        heapq.heapify(sumQueue)

        res = 0

        while violations > 0 and sumQueue:
            val, id, left, right = heapq.heappop(sumQueue)

            currentVal = left.val
            if right:
                currentVal += right.val

            # already processed
            if val != currentVal or left.right != right or (right and right.left != left):
                continue

            res += 1

            # remove old violations
            if left.left and left.left.val > left.val:
                violations -= 1
            if left.right and left.val > left.right.val:
                violations -= 1
            if right and right.right and right.val > right.right.val:
                violations -= 1

            rightVal = 0 if not left.right else left.right.val

            # merge
            left.val = left.val + rightVal
            nextRight = None if not left.right else left.right.right
            left.right = nextRight

            if nextRight:
                nextRight.left = left

            # add new violance
            if left.left and left.left.val > left.val:
                violations += 1
            if left.right and left.val > left.right.val:
                violations += 1

            if left.left:
                heapq.heappush(sumQueue, (
                    left.val + left.left.val,
                    left.left.id,
                    left.left,
                    left,
                ))
            if left.right:
                heapq.heappush(sumQueue, (
                    left.val + left.right.val,
                    left.id,
                    left,
                    left.right,
                ))


        return res



'''

[5,2,3,1]
5, 2, 3, 1
5, 5, 1
5, 6

10, 11, 12, 10, 9, 8, 7
10, 11, 12, 10, 9, 15
10, 11, 12, 19, 15
10, 11, 12, 34

10, 11, 12, 10, 9, 8, 7
10, 11, 12, 10, 9, 15
10, 11, 12, 19, 15
21, 12, 19, 15
21, 31, 15
21, 46

'''


def test():
    params = [
        {
            "input": [5,2,3,1],
            "output": 2,
        },
        {
            "input": [1,2,2],
            "output": 0,
        },
        {
            "input": [10, 11, 12, 10, 9, 8, 7],
            "output": 5,
        },
        {
            "input": [2,2,-1,3,-2,2,1,1,1,0,-1],
            "output": 9,
        },
        {
            "input": [0,-1,-1,-1,1,0,-1],
            "output": 9,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param["input"]
        result = solution.minimumPairRemoval(nums)
        correct = json.dumps(result) == json.dumps(param["output"])

        msg = "SUCCESS" if correct else "ERROR"
        msg += "\n"
        if not correct:
            # msg += "input " + json.dumps(param["input"]) + "\n"
            msg += "output " + json.dumps(param["output"]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

        print(msg)


if __name__ == "__main__":
    test()
