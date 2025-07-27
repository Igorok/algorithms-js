function minimumScore(nums: number[], edges: number[][]): number {
    const adj: number[][] = new Array(nums.length).fill(0).map(() => []);
    let root: number = 0;
    for (const [s, e] of edges) {
        adj[s].push(e);
        adj[e].push(s);

        if (adj[s].length > adj[root].length) {
            root = s;
        }
        if (adj[e].length > adj[root].length) {
            root = s;
        }
    }

    const nodeXor: number[] = new Array(nums.length).fill(0);
    const calculateXor = (node: number, visited: number[]) => {
        nodeXor[node] = nums[node];

        for (const nei of adj[node]) {
            if (visited[nei]) {
                continue;
            }

            visited[nei] = 1;
            const x: number = calculateXor(nei, visited);
            nodeXor[node] ^= x;
        }


        return nodeXor[node];
    };

    let visited: number[] = new Array(nums.length).fill(0);
    visited[root] = 1;
    calculateXor(root, visited);

    let res: number = Number.MAX_SAFE_INTEGER;

    const dfs = (node: number, visited: number[], cutNode: number) => {
        const firstXor: number = nodeXor[cutNode];

        let cutted: boolean = false;

        for (const nei of adj[node]) {
            if (nei === cutNode) {
                return true;
            }
            if (visited[nei]) {
                continue;
            }

            visited[nei] = 1;

            let r = dfs(nei, visited, cutNode);
            cutted = cutted || r;

            const secondXor: number = r
                ? nodeXor[nei] ^ nodeXor[cutNode]
                : nodeXor[nei];
            const thirdXor: number = r
                ? nodeXor[root] ^ nodeXor[nei]
                : nodeXor[root] ^ nodeXor[cutNode] ^ nodeXor[nei];

            const max: number = Math.max(firstXor, secondXor, thirdXor);
            const min: number = Math.min(firstXor, secondXor, thirdXor);
            res = Math.min(res, max - min);
        }

        return cutted;
    };

    for (let i: number = 0; i < nums.length; ++i) {
        if (i === root) {
            continue;
        }

        visited = new Array(nums.length).fill(0);
        visited[root] = 1;
        visited[i] = 1;
        dfs(root, visited, i);
    }

    return res;
};


/*

101
010
111

101=5
^
010=2
^
111=7
000




*/

const test = () => {
    const params = [
        {
            input: {
                nums: [28,24,29,16,31,31,17,18],
                edges: [[0,1],[6,0],[6,5],[6,7],[3,0],[2,1],[2,4]],
            },
            output: 8,
        },
        {
            input: {
                nums: [1,5,5,4,11],
                edges: [[0,1],[1,2],[1,3],[3,4]],
            },
            output: 9,
        },
        {
            input: {
                nums: [5,5,2,4,4,2],
                edges: [[0,1],[1,2],[5,2],[4,3],[1,3]],
            },
            output: 0,
        },

    ];

    params.forEach(({input, output}) => {
        const { nums, edges } = input;

        const result = minimumScore(nums, edges);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();