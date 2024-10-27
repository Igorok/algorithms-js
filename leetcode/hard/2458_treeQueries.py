# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        deeps = {}
        levels = {}
        topOnLevel = {}

        def setTopOnLevel(node, level, deep):
            dOnl = topOnLevel[level]
            if dOnl[0] == -1:
                dOnl[0] = deep
            else:
                if dOnl[0] < deep:
                    dOnl[0], dOnl[1] = deep, dOnl[0]
                elif dOnl[1] == -1 or dOnl[1] < deep:
                    dOnl[1] = deep

        def dfs(node, level):
            levels[node.val] = level
            if not level in topOnLevel:
                topOnLevel[level] = [-1, -1]

            if not node.left and not node.right:
                deeps[node.val] = 0
                setTopOnLevel(node, level, 0)
                return 0

            ld = 0
            rd = 0

            if node.left:
                ld = dfs(node.left, level + 1)
            if node.right:
                rd = dfs(node.right, level + 1)

            d = max(ld, rd) + 1
            deeps[node.val] = d

            setTopOnLevel(node, level, d)
            return d

        d = dfs(root, 0)

        # print(
        #     'parents', parents,
        #     'deeps', deeps,
        #     'levels', levels,
        #     'topOnLevel', topOnLevel,
        # )

        res = []


        def getNewDeep(q):
            nonlocal res

            deep = deeps[q]
            level = levels[q]
            top = topOnLevel[level]
            if deep < top[0] or top[0] == top[1]:
                res.append(topOnLevel[0][0])
            else:
                prev = topOnLevel[0][0]
                diff = top[0] - top[1]
                res.append(prev - diff)



        for q in queries:
            getNewDeep(q)


        return res
