/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var findChampion = function(n, edges) {
    const adj = new Array(n).fill(0);
    for (const [s, e] of edges) {
        if (!adj[e]) adj[e] = 0;
        adj[e] += 1;
    }

    const champions = [];
    for (let s = 0; s < n; ++s) {
        if (!adj[s]) champions.push(s);
    }

    return (champions.length === 1) ? champions[0] : -1;
};

/*

0 - 1 - 2





*/

const test = () => {
    const params = [
        {
            input: [3, [[0,1],[1,2]]],
            output: 0,
        },
        {
            input: [4, [[0,2],[1,3],[1,2]]],
            output: -1,
        },
        {
            input: [1, []],
            output: 0,
        },
    ];

    for (const { input, output } of params) {
        const result = findChampion(...input);
        const message = `
            INPUT: ${JSON.stringify(input)}
            OUTPUT: ${output}
            RESULT: ${result}
            `;

        if (JSON.stringify(result) === JSON.stringify(output)) {
            console.log(
                'SUCCESS: \n', message,
            );
        } else {
            console.error('ERROR: \n', message);
        }
    }
};

test();
