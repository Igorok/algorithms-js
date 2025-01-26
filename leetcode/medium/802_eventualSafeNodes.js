/**
 * @param {number[][]} graph
 * @return {number[]}
 */
var eventualSafeNodes_0 = function(graph) {
    const safeNodes = new Array(graph.length).fill(-1);

    const dfs = (id, visited) => {
        if (safeNodes[id] !== -1) {
            return safeNodes[id];
        }
        if (visited[id] === 1) {
            return 0;
        }
        visited[id] = 1;

        for (let i of graph[id]) {
            const r = dfs(i, visited);
            if (r === 0) {
                safeNodes[id] = 0;
                return 0;
            }
        }

        visited[id] = 0;

        safeNodes[id] = 1;
        return safeNodes[id];
    };

    for (let i = 0; i < graph.length; ++i) {
        if (!graph[i].length) {
            safeNodes[i] = 1;
            continue;
        }
        if (safeNodes[i] !== -1) {
            continue;
        }
        dfs(i, new Array(graph.length).fill(0));
    }
    const res = [];
    for (let i = 0; i < graph.length; ++i) {
        if (safeNodes[i] === 1) {
            res.push(i);
        }
    }
    return res;
};

var eventualSafeNodes = function(graph) {
    const safeNodes = new Array(graph.length).fill(-1);

    const dfs = (id) => {
        if (safeNodes[id] !== -1) {
            return safeNodes[id];
        }
        safeNodes[id] = 0;

        for (let i of graph[id]) {
            const r = dfs(i);
            if (r === 0) {
                safeNodes[id] = 0;
                return 0;
            }
        }

        safeNodes[id] = 1;
        return safeNodes[id];
    };

    const res = [];
    for (let i = 0; i < graph.length; ++i) {
        if (!graph[i].length) {
            safeNodes[i] = 1;
            res.push(i);
            continue;
        }
        if (safeNodes[i] === 1) {
            res.push(i);
            continue;
        }
        if (safeNodes[i] === -1) {
            const r = dfs(i);
            if (r === 1) {
                res.push(i);
            }
        }
    }
    return res;
};

const test = () => {
    const params = [
        {
            input: [[1,2],[2,3],[5],[0],[5],[],[]],
            output: [2,4,5,6],
        },
        {
            input: [[1,2,3,4],[1,2],[3,4],[0,4],[]],
            output: [4],
        },
    ];

    for (const { input, output } of params) {
        const result = eventualSafeNodes(input);
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
