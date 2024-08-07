/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */

const isSymmetricNodes = (node1, node2) => {
    if (!node1 && !node2) return true;

    if (node1?.val !== node2?.val) return false;

    if (!isSymmetricNodes(node1.left, node2.right) || !isSymmetricNodes(node1.right, node2.left)) {
        return false;
    }

    return true;
};

var isSymmetric = function(root) {
    if (!root) return true;

    return isSymmetricNodes(root.left, root.right);
};
