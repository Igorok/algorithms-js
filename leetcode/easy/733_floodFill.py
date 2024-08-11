from typing import List
import json

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        startColor = image[sr][sc]
        def dfs (i, j):
            if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or image[i][j] != startColor:
                return

            image[i][j] = color
            neighbor = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
            for y, x in neighbor:
                dfs(y, x)

        dfs(sr, sc)

        return image




def test ():
    params = [
        {
            'input': [[[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2],
            'output': [[2,2,2],[2,2,0],[2,0,1]],
        },
        {
            'input': [[[0,0,0],[0,0,0]], 0, 0, 0],
            'output': [[0,0,0],[0,0,0]],
        },
        {
            'input': [[[0,0,0],[0,0,0]], 1, 0, 2],
            'output': [[2,2,2],[2,2,2]],
        },
    ]
    solution = Solution()

    for param in params:
        arr, sr, sc, color = param['input']
        result = solution.floodFill(arr, sr, sc, color)
        print(
            'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
