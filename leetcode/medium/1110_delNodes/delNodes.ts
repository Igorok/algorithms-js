class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function delNodes(root: TreeNode | null, to_delete: number[]): Array<TreeNode | null> {
    if (!root) return [];
    if (!to_delete?.length) return [root];

    const result: TreeNode[] = (!to_delete.includes(root.val)) ? [root] : [];

    const stack: { node: TreeNode, parent: TreeNode | null }[] = [
        { node: root, parent: null },
    ];

    while (stack.length) {
        const { node, parent } = stack.pop();

        console.log({ node, parent });
        console.log(
            'node?.val', node?.val,
            'parent?.val', parent?.val,
        );


        const deleted: boolean = to_delete.includes(node.val);

        if (node.left) {
            stack.push({ node: node.left, parent: node });
        }
        if (node.right) {
            stack.push({ node: node.left, parent: node });
        }

        if (deleted) {
            if (parent) {
                if (node == parent.left) {
                    parent.left = null;
                } else {
                    parent.right = null;
                }
            }


            if (node.left) {
                result.push(node.left);
            }
            if (node.right) {
                result.push(node.right);
            }
        }
    }



    return result;
};
