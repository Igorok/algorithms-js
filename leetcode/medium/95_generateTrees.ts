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

function generateTrees(n: number): Array<TreeNode | null> {
    const rec = (left: number, right: number): Array<TreeNode | null> => {
        if (left === right) {
            return [new TreeNode(left)];
        }

        if (left > right) {
            return [null];
        }

        const allNodes: Array<TreeNode | null> = [];

        for (let i = left; i <= right; ++i) {
            const leftNodes = rec(left, i-1);
            const rightNodes = rec(i+1, right);

            for (let l of leftNodes) {
                for (let r of rightNodes) {
                    const node = new TreeNode(i);
                    node.left = l;
                    node.right = r;

                    allNodes.push(node);
                }
            }
        }

        return allNodes;
    };

    return rec(1, n);
};


/*

1 2 3 4 5 6 7 8

*/

const test = () => {
    const params = [
        {
            input: 3,
            output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]],
        },
        {
            input: 1,
            output: [[1]],
        },
    ];

    params.forEach(({input, output}) => {
        const result = generateTrees(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();