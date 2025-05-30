function maxTargetNodes(edges1: number[][], edges2: number[][], k: number): number[] {
    const adj1: number[][] = new Array(edges1.length + 1).fill(0).map(() => []);
    const adj2: number[][] = new Array(edges2.length + 1).fill(0).map(() => []);

    for (const [s, e] of edges1) {
        adj1[s].push(e);
        adj1[e].push(s);
    }

    for (const [s, e] of edges2) {
        adj2[s].push(e);
        adj2[e].push(s);
    }

    const getCount = (adj: number[][], id: number, step: number, parent: number): number => {
        if (step < 0) {
            return 0;
        }
        if (step === 0) {
            return 1;
        }
        let res: number = 1;
        for (const nei of adj[id]) {
            if (nei !== parent) {
                res += getCount(adj, nei, step - 1, id);
            }
        }
        return res;
    };

    const countOfTarget2: number[] = new Array(edges2.length + 1).fill(0);
    let maxCount: number = 0;
    if (k - 1 >= 0) {
        for (let i: number = 0; i < countOfTarget2.length; ++i) {
            countOfTarget2[i] += getCount(adj2, i, k-1, i);
            maxCount = Math.max(maxCount, countOfTarget2[i]);
        }
    }

    const res: number[] = new Array(edges1.length + 1).fill(0);
    for (let i: number = 0; i < res.length; ++i) {
        const count: number = getCount(adj1, i, k, i);
        res[i] = count + maxCount;
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                edges1: [[0,1]],
                edges2: [[0,1]],
                k: 0
            },
            output: [1,1],
        },
        {
            input: {
                edges1: [[0,1],[0,2],[2,3],[2,4]],
                edges2: [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]],
                k: 2
            },
            output: [9,7,9,8,8],
        },
        {
            input: {
                edges1: [[0,1],[0,2],[0,3],[0,4]],
                edges2: [[0,1],[1,2],[2,3]],
                k: 1
            },
            output: [6,3,3,3,3],
        },
    ];

    params.forEach(({input, output}) => {
        const {edges1, edges2, k} = input;
        const result = maxTargetNodes(edges1, edges2, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();