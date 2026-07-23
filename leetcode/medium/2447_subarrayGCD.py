import heapq
from collections import Counter, defaultdict
from functools import cache
from json import dumps
from typing import List



'''
Yes, it is a universal mathematical property! You can think of it as a chain reaction. You don’t need to compare every single number against every other number to find the common factor of the whole group.Instead, the GCD operation is associative. This means you can group the numbers however you like, and moving from left to right yields the exact same result:gcd(a, b, c, d) = gcd(gcd(gcd(a, b), c), d)
'''

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def getGcd(a,b):
            a,b = (a,b) if a >= b else (b,a)
            r = a%b
            if r == 0:
                return b
            return getGcd(b,r)

        N = len(nums)
        res = 0
        for i in range(N):
            val = nums[i]
            for j in range(i,N):
                val = getGcd(val, nums[j])
                if val == k:
                    res += 1
            
        return res
        
'''
Do you know a leetcode issue "2447. Number of Subarrays With GCD Equal to K"?

Where i can find here 10 subsecuent array with gcd 1?
[[3,3,4,1,2], 1]
3,4 - 1
3,3,4,1 - 3
1,2 - 1

'''
        
        
        
def test():
    params = [
        {
            "input": [[9,3,1,2,6,3], 3],
            "output": 4,
        },
        {
            "input": [[4], 7],
            "output": 0,
        },
        {
            "input": [[3,3,4,1,2], 1],
            "output": 10,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param["input"]
        result = solution.subarrayGCD(nums, k)
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
