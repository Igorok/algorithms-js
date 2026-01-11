from typing import List
import heapq


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)
        S = sum(nums)
        memo = [[-1]*(N+2) for i in range(N+2)]


        def dfs(id1, id2):
            if id1 > id2:
                return 0
            if id1 == id2:
                return nums[id1]

            if memo[id1][id2] != -1:
                return memo[id1][id2]

            # first id1
            r1 = nums[id1] + min(
                # second id1+1
                dfs(id1+2, id2),
                # second id2
                dfs(id1+1, id2-1)
            )

            # first id2
            r2 = nums[id2] + min(
                # second id1
                dfs(id1+1, id2-1),
                #second id2-1
                dfs(id1, id2-2)
            )

            memo[id1][id2] = max(r1, r2)

            return memo[id1][id2]

        r = dfs(0, N-1)

        return S - r <= r




def test ():
    params = [
        {
            'input': [1,5,2],
            'output': False,
        },
        {
            'input': [1,5,233,7],
            'output': True,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.predictTheWinner(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
