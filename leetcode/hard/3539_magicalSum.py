from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        # return (x**y)%mod
        def quickmul(x, y, mod):
            res = 1
            while y > 0:
                if y & 1:
                    res = (res * x) % mod
                x = (x*x) % mod
                y = y >> 1
            return res

        # print(
        #     '2**5', quickmul(2, 5, mod)
        # )

        n = len(nums)
        mod = 7 + 10**9

        # list factorials
        fac = [1] * (m+1)
        for i in range(2, m+1):
            fac[i] = (i * fac[i-1]) % mod

        # fermat theorem
        # (x(mod y))**-1 = (x**y-2)(mod y)
        ifac = [1] * (m+1)
        # calculate every number x**(y-2)
        for i in range(2, m+1):
            ifac[i] = quickmul(i, mod-2, mod)
        # calculate factorials from numbers x**(y-2)
        for i in range(2, m+1):
            ifac[i] = (ifac[i-1] * ifac[i]) % mod

        # accumulate all powers of possible numbers
        nums_power = [[1] * (m+1) for _ in range(n)]
        for i in range(n):
            for j in range(1, m+1):
                nums_power[i][j] = (nums_power[i][j-1] * nums[i]) % mod

         # DP state dp_table[idx_i][total_count][prev_carry_raw][set_bits_counted]:
        # idx_i: Index (exponent 2^i) currently being processed. 0 <= idx_i < n.
        # total_count: Total number of indices chosen so far (sum(c_l for l=0 to i)). 0 <= total_count <= m.
        # prev_carry_raw: The "raw count" or coefficient at position 2^i, which is (c_i + carry_in).
        #                 This state simplifies binary addition simulation. Max size is 2*m+1.
        # set_bits_counted: Number of set bits (1s) found in the binary sum N up to position 2^(i-1). 0 <= set_bits_counted <= k.
        # Value: The accumulated sum of products, normalized by factorials: sum( product( (nums[l]**c_l) / c_l! ) ).


        return 0

'''
2**5
1
x=2; res = 1*2=2; d=5;
x=2*2=4; res=2; d=2;
x=4**2=16; res=8*16=; d=0;



'''

def test():
    params = [
        {
            "input": [5, 5, [1,10,100,10000,1000000]],
            "output": 991600007,
        },
        {
            "input": [2, 2, [5,4,3,2,1]],
            "output": 170,
        },
        {
            "input": [1, 1, [28]],
            "output": 28,
        },
    ]
    solution = Solution()

    for param in params:
        m, k, nums = param["input"]
        result = solution.magicalSum(m, k, nums)
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
