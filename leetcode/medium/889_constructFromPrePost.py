from typing import List
from json import dumps
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def dfs(preorder, postorder):
            rootNum = preorder[0]
            root = TreeNode(rootNum)

            preorder = preorder[1:]
            postorder = postorder[:len(postorder)-1]
            if not len(preorder):
                return root

            leftChildPostId = postorder.index(preorder[0])
            leftPreOrder = preorder[:leftChildPostId+1]
            leftPostOrder = postorder[:leftChildPostId+1]
            root.left = dfs(leftPreOrder, leftPostOrder)

            if len(leftPreOrder) != len(preorder):
                rightPreOrder = preorder[leftChildPostId+1:]
                rightPostOrder = postorder[leftChildPostId+1:]
                rott.right = dfs(rightPreOrder, rightPostOrder)

            return root

        return dfs(preorder, postorder)

def test ():
    params = [
        {
            'input': [[1,2,4,5,3,6,7], [4,5,2,6,7,3,1]],
            'output': [1,2,3,4,5,6,7],
        },
        {
            'input': [[1], [1]],
            'output': [1],
        },
    ]
    solution = Solution()

    for param in params:
        preorder, postorder = param['input']
        result = solution.minPathSum(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
