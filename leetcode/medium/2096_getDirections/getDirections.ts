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

const getParent = (root: TreeNode | null, startValue: number, destValue: number): TreeNode => {
    if (root.val === startValue || root.val === destValue) {
        return root;
    }

    let left: TreeNode | null = null;
    let right: TreeNode | null = null;
    if (root.left)
        left = getParent(root.left, startValue, destValue);
    if (root.right)
        right = getParent(root.right, startValue, destValue);

    if (left && right) return root;
    else if (left) return left;
    else return right;
};

const getPath = (root: TreeNode | null, query: number, path: string[]): boolean => {
    if (root.val == query)
        return true;

    if (root.left) {
        const result: boolean = getPath(root.left, query, path);
        if (result) {
            path.push('L');
            return result;
        }
    }

    if (root.right) {
        const result: boolean = getPath(root.right, query, path);
        if (result) {
            path.push('R');
            return result;
        }
    }

    return false;
};

function getDirections(root: TreeNode | null, startValue: number, destValue: number): string {
    if (!root) return '';

    const parent = getParent(root, startValue, destValue);

    let startPath: string[] = [];
    let endPath: string[] = [];

    getPath(parent, startValue, startPath);
    getPath(parent, destValue, endPath);

    if (startPath.length)
        startPath = new Array(startPath.length).fill('U');
    if (endPath.length)
        endPath = endPath.reverse();

    return startPath.concat(endPath).join('');
};
