var TreeNode = /** @class */ (function () {
    function TreeNode(val, left, right) {
        this.val = (val === undefined ? 0 : val);
        this.left = (left === undefined ? null : left);
        this.right = (right === undefined ? null : right);
    }
    return TreeNode;
}());
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
function delNodes(root, to_delete) {
    if (!root)
        return [];
    if (!(to_delete === null || to_delete === void 0 ? void 0 : to_delete.length))
        return [root];
    var result = (!to_delete.includes(root.val)) ? [root] : [];
    var stack = [
        { node: root, parent: null },
    ];
    while (stack.length) {
        var _a = stack.pop(), node = _a.node, parent_1 = _a.parent;
        console.log({ node: node, parent: parent_1 });
        console.log('node?.val', node === null || node === void 0 ? void 0 : node.val, 'parent?.val', parent_1 === null || parent_1 === void 0 ? void 0 : parent_1.val);
        var deleted = to_delete.includes(node.val);
        if (node.left) {
            stack.push({ node: node.left, parent: node });
        }
        if (node.right) {
            stack.push({ node: node.left, parent: node });
        }
        if (deleted) {
            if (parent_1) {
                if (node == parent_1.left) {
                    parent_1.left = null;
                }
                else {
                    parent_1.right = null;
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
}
;
