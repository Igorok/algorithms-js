from typing import List
import json
from collections import deque, defaultdict
from functools import lru_cache

class Solution_0:
    """
    Solves the 'Find Sum of Array Product of Magical Sequences' problem using Dynamic Programming.

    The core idea is to simulate the binary addition required by the magical condition:
    N = sum(c_j * 2^j), where c_j is the count of index j in the sequence (sum(c_j) = m).
    The DP simultaneously tracks:
    1. The total count used (must equal m).
    2. The carry propagating through the binary addition.
    3. The number of set bits (1s) found so far (must equal k).

    The accumulated value in the DP state is the sum of products, normalized by 1/c_j!,
    which is corrected by multiplying by m! at the end (Multinomial Theorem).
    """

    def quickmul(self, x: int, y: int, mod: int) -> int:
        """
        Calculates (x^y) % mod using binary exponentiation.
        This is used to find modular inverses (a^-1) for division modulo P.
        """
        res, cur = 1, x % mod
        while y:
            if y & 1:
                res = res * cur % mod
            y >>= 1
            cur = cur * cur % mod
        return res

    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        mod = 10**9 + 7

        # --- Pre-computation 1: Factorials and Inverse Factorials ---

        # fac[i] = i! % mod
        fac = [1] * (m + 1)
        for i in range(1, m + 1):
            fac[i] = fac[i - 1] * i % mod

        # inv_fac[i] = (1/i!) % mod. Essential for the Multinomial Theorem.
        inv_fac = [1] * (m + 1)
        inv_fac[0] = 1 # 1/0!
        inv_fac[1] = 1 # 1/1!

        # Step 1: Calculate the modular inverse for each number i (i.e., 1/i % mod)
        #         and store it temporarily in inv_fac[i].
        for i in range(2, m + 1):
            # Using Fermat's Little Theorem: i^(mod-2) = i^-1 mod mod
            inv_fac[i] = self.quickmul(i, mod - 2, mod)

        # Step 2: Calculate the cumulative inverse factorial (i!)^-1 iteratively.
        # inv_fac[i] = inv_fac[i-1] * (1/i) = 1/((i-1)!) * (1/i) = 1/i!
        for i in range(2, m + 1):
            inv_fac[i] = inv_fac[i - 1] * inv_fac[i] % mod


        # --- Pre-computation 2: Powers of nums[i] ---

        # nums_power[i][j] = (nums[i] ** j) % mod. Used to quickly get the product factor.
        nums_power = [[1] * (m + 1) for _ in range(n)]
        for i in range(n):
            for j in range(1, m + 1):
                nums_power[i][j] = nums_power[i][j - 1] * nums[i] % mod

        # --- Dynamic Programming Setup ---

        # DP state dp_table[idx_i][total_count][prev_carry_raw][set_bits_counted]:
        # idx_i: Index (exponent 2^i) currently being processed. 0 <= idx_i < n.
        # total_count: Total number of indices chosen so far (sum(c_l for l=0 to i)). 0 <= total_count <= m.
        # prev_carry_raw: The "raw count" or coefficient at position 2^i, which is (c_i + carry_in).
        #                 This state simplifies binary addition simulation. Max size is 2*m+1.
        # set_bits_counted: Number of set bits (1s) found in the binary sum N up to position 2^(i-1). 0 <= set_bits_counted <= k.
        # Value: The accumulated sum of products, normalized by factorials: sum( product( (nums[l]**c_l) / c_l! ) ).

        MAX_CARRY_STATE = m * 2 + 1

        dp_table = [
            [[[0] * (k + 1) for _ in range(MAX_CARRY_STATE)] for _ in range(m + 1)]
            for _ in range(n)
        ]

        # --- Base Case: Processing the first index idx_i=0 (exponent 2^0) ---

        # Iterate over c0 (the count of index 0)
        for c0 in range(m + 1):
            # c0: total_count used (c0)
            # c0: raw carry state (c0 + 0 carry_in)
            # 0: set bits found before index 0
            dp_table[0][c0][c0][0] = nums_power[0][c0] * inv_fac[c0] % mod


        # --- DP Transition (from index idx_i to idx_i+1) ---

        # idx_i: current index/exponent we are transitioning FROM
        for idx_i in range(n - 1):
            for total_count_prev in range(m + 1):
                for prev_carry_raw in range(MAX_CARRY_STATE):
                    for prev_set_bits in range(k + 1):

                        current_value = dp_table[idx_i][total_count_prev][prev_carry_raw][prev_set_bits]
                        if current_value == 0:
                            continue

                        # 1. Determine the bit and carry generated at the current position idx_i

                        # bit_i: The bit at position 2^idx_i (i.e., (c_i + carry_in) % 2)
                        bit_i = prev_carry_raw % 2

                        # carry_to_next: The carry propagating to position 2^(idx_i+1)
                        carry_to_next = prev_carry_raw // 2

                        # total_set_bits_up_to_i: set bits found up to index idx_i
                        total_set_bits_up_to_i = bit_i + prev_set_bits

                        if total_set_bits_up_to_i > k:
                            # Optimization: if k is exceeded, this path is invalid
                            continue

                        # 2. Iterate over the choice c_next = c_{idx_i+1} for the next index
                        for c_next in range(m - total_count_prev + 1):

                            # next_carry_raw: The raw sum at position (idx_i + 1) before division by 2
                            # next_carry_raw = (carry_from_i) + (new_coefficient c_next)
                            next_carry_raw = carry_to_next + c_next

                            if next_carry_raw >= MAX_CARRY_STATE:
                                # Optimization: carry is too large for the state size
                                continue

                            new_total_count = total_count_prev + c_next

                            # 3. Calculate the product factor: (nums[idx_i+1] ^ c_next) * (1 / c_next!)
                            factor = (
                                nums_power[idx_i + 1][c_next]
                                * inv_fac[c_next]
                                % mod
                            )

                            term = current_value * factor % mod

                            # 4. Update the next state:
                            dp_table[idx_i + 1][new_total_count][next_carry_raw][total_set_bits_up_to_i] = (
                                dp_table[idx_i + 1][new_total_count][next_carry_raw][total_set_bits_up_to_i]
                                + term
                            ) % mod

        # --- Final Result Calculation ---

        final_idx = n - 1
        final_sum_of_products = 0

        # Check all possible final carry states and set bit counts
        # We must ensure the total count is exactly m
        for remaining_carry_raw in range(MAX_CARRY_STATE):
            for set_bits_counted in range(k + 1):

                # The total set bits K is composed of:
                # 1. set_bits_counted (q): Set bits found up to position n-1 (from the transition logic).
                # 2. set bits in remaining_carry_raw (p): The final carry represents higher-order bits (2^n, 2^(n+1), etc.).

                remaining_set_bits = bin(remaining_carry_raw).count("1")

                if remaining_set_bits + set_bits_counted == k:

                    # Accumulate the normalized sum from the DP table
                    normalized_sum = dp_table[final_idx][m][remaining_carry_raw][set_bits_counted]

                    # Final step: Multiply by m! to undo the (1/c_j!) normalization (Multinomial Theorem).
                    res_term = normalized_sum * fac[m] % mod
                    final_sum_of_products = (final_sum_of_products + res_term) % mod

        return final_sum_of_products



class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        mod = 7 + 10**9
        n = len(nums)
        numsPower = [[1] * (m+1) for i in range(n)]
        for i in range(n):
            for j in range(1, m+1):
                numsPower[i][j] = (numsPower[i][j-1] * nums[i]) % mod

        factorials = [1 for i in range(m+1)]
        for i in range(2, m+1):
            factorials[i] = (i * factorials[i-1]) % mod

        # how many bit will have new number?
        def getBits(carry):
            res = 0
            while carry > 0:
                res += (carry & 1)
                carry >>= 1
            return res

        # return (x**y)%mod
        def quickpower(x: int, y: int, mod: int) -> int:
            res = 1
            while y > 0:
                if y & 1:
                    res = (res * x) % mod
                x = (x ** 2) % mod
                y >>= 1

            return res

        # inv_fac[i] = (1/i!) % mod. Essential for the Multinomial Theorem.
        inv_fac = [1] * (m + 1)

        # Step 1: Calculate the modular inverse for each number i (i.e., 1/i % mod)
        #         and store it temporarily in inv_fac[i].
        for i in range(2, m + 1):
            # Using Fermat's Little Theorem: i^(mod-2) = i^-1 mod mod
            inv_fac[i] = quickpower(i, mod - 2, mod)

        # Step 2: Calculate the cumulative inverse factorial (i!)^-1 iteratively.
        # inv_fac[i] = inv_fac[i-1] * (1/i) = 1/((i-1)!) * (1/i) = 1/i!
        for i in range(2, m + 1):
            inv_fac[i] = inv_fac[i - 1] * inv_fac[i] % mod

        @lru_cache(None)
        def dfs(id, used, carry, bits):
            if id == n:
                countOfBits = bits + getBits(carry)
                return 1 if countOfBits == k and used == m else 0

            res = 0

            available = m - used
            for cnt in range(available + 1):
                bit = ((cnt + carry) & 1)
                newUsed = used + cnt
                # what is new carry? old carry + new bits will carrying forward, prev position skipped
                newCarry = ((carry + cnt) >> 1)
                newBits = bits + bit

                r = dfs(id + 1, newUsed, newCarry, newBits)
                if r == 0:
                    continue

                num = nums[id]

                currentPower = numsPower[id][cnt]
                combinations = factorials[available] * inv_fac[available-cnt] % mod
                combinations = combinations * inv_fac[cnt] % mod


                impact = (currentPower * combinations) % mod
                impact = (r * impact) % mod
                res = (res + impact) % mod

            return res


        return dfs(0, 0, 0, 0)

'''
3 = 011
001
001
=
010

010
001
=
011

---



'''



def test():
    params = [
        {
            "input": [2, 2, [5,4,3,2,1]],
            "output": 170,
        },
        {
            "input": [1, 1, [28]],
            "output": 28,
        },

        {
            "input": [5, 5, [1,10,100,10000,1000000]],
            "output": 991600007,
        },
        {
            "input": [10, 6, [79,8,75,37,81]],
            "output": 599614523,
        },
        {
            "input": [13, 8, [52900,36842,43727,57290,97561,94545,84642,68215,91601,76832,52673,94789,6123,70762,73080,11830,57262,93991,95078,95082,58420,62723]],
            "output": 120815395,
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
