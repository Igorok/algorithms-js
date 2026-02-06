from typing import List
import json
import heapq


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        res = 0

        left = 0
        cnt = 0
        local = 0

        for right in range(N):
            if (nums[right] % 2) == 1:
                cnt += 1

            if cnt == k:
                local += 1
                continue

            if cnt > k:
                while cnt > k:
                    res += local
                    if (nums[left] % 2) == 1:
                        cnt -= 1
                    left += 1

                local = 1

        while cnt >= k:
            res += local
            if (nums[left] % 2) == 1:
                cnt -= 1
            left += 1

        return res


def test ():
    params = [
        {
            'input': [[1,1,2,1,1], 3],
            'output': 2,
        },
        {
            'input': [[2,4,6], 1],
            'output': 0,
        },
        {
            'input': [[2,2,2,1,2,2,1,2,2,2], 2],
            'output': 16,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']
        result = solution.numberOfSubarrays(nums, k)
        print(
            'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
