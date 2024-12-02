/**
 * @param {number[][]} pairs
 * @return {number[][]}
 */
var validArrangement = function(pairs) {
    const adj = new Map();
    const input = new Map();
    const output = new Map();
    const nodes = new Set();

    for (const [s, e] of pairs) {
        const vertexes = adj.get(s) || [];
        vertexes.push(e);
        adj.set(s, vertexes);

        const o = (output.get(s) || 0) + 1;
        output.set(s, o);

        const i = (input.get(e) || 0) + 1;
        input.set(e, i);

        nodes.add(s);
        nodes.add(e);
    }

    let startNode = -1;
    for (const node of nodes.values()) {
        const i = input.get(node) || 0;
        const o = output.get(node) || 0;

        startNode = node;
        if (o - i === 1) {
            break;
        }
    }

    const eulerPath = [];
    const findPath = (node) => {
        while (output.get(node) > 0) {
            const o = output.get(node) - 1;
            output.set(node, o);

            const path = adj.get(node);
            const nei = path[o];
            findPath(nei);
        }
        eulerPath.push(node);
    };

    findPath(startNode);

    const result = [];

    for (let i = eulerPath.length - 1; i > 0; --i) {
        result.push([eulerPath[i], eulerPath[i - 1]]);
    }

    return result;
};

/*
.


ERROR  input
[[8,5],[8,7],[0,8],[0,5],[7,0],[5,0],[0,7],[8,0],[7,8]]
output
[[8,0],[0,7],[7,8],[8,7],[7,0],[0,5],[5,0],[0,8],[8,5]]
result
[[8,5],[5,7],[7,0],[0,8],[8,5],[5,7],[7,0],[0,8],[8,5],[5,7],[7,0],[0,8],[8,5],[5,0],[0,8],[8,5]]




*/

const test = () => {
    const params = [
        // {
        //     input: [[5,1],[4,5],[11,9],[9,4]],
        //     output: [[11,9],[9,4],[4,5],[5,1]],
        // },
        // {
        //     input: [[1,3],[3,2],[2,1]],
        //     output: [[1,3],[3,2],[2,1]],
        // },
        // {
        //     input: [[1,2],[1,3],[2,1]],
        //     output: [[1,2],[2,1],[1,3]],
        // },

        {
            input: [[8,5],[8,7],[0,8],[0,5],[7,0],[5,0],[0,7],[8,0],[7,8]],
            output: [[8,0],[0,7],[7,8],[8,7],[7,0],[0,5],[5,0],[0,8],[8,5]],
        },
    ];

    params.forEach(({input, output}) => {
        const result = validArrangement(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();