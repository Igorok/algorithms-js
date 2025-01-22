/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function(preorder, inorder) {
    function TreeNode(val, left, right) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }

    const rec = (preorder, inorder) => {
        if (!preorder.length) {
            return null;
        }
        const num = preorder[0];
        const root = new TreeNode(num);

        const id = inorder.findIndex((val) => val === num);
        const leftInorder = inorder.slice(0, id);
        const rightInorder = inorder.slice(id + 1);

        const leftPreorder = leftInorder.length ? preorder.slice(1, id + 1) : [];
        const rightPreorder = rightInorder.length ? preorder.slice(id + 1) : [];


        root.left = rec(leftPreorder, leftInorder);
        root.right = rec(rightPreorder, rightInorder);
        return root;
    };

    return rec(preorder, inorder);
};


const test = () => {
    const params = [
        {
            input: [[3,9,20,15,7], [9,3,15,20,7]],
            output: [3,9,20,null,null,15,7],
        },
        {
            input: [[-1], [-1]],
            output: [-1],
        },
        {
            input: [[3,9,8,10,20,15,7], [8,9,10,3,15,20,7]],
            output: [3,9,20,null,null,15,7],
        },
        {
            input: [[1,2], [1,2]],
            output: [1,2],
        },
        {
            input: [[1,2,3], [3,2,1]],
            output: [1,2,3,null,2],
        },
    ];


    for (const { input, output } of params) {
        const result = buildTree(...input);
        const message = `
            INPUT: ${JSON.stringify(input)}
            OUTPUT: ${JSON.stringify(output)}
            RESULT: ${JSON.stringify(result)}`;

        if (JSON.stringify(result) === JSON.stringify(output)) {
            console.log(
                `SUCCESS: ${message}`,
            );
        } else {
            console.error(`ERROR: ${message}`);
        }
    }
};

test();
