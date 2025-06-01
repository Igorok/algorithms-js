function numOfMinutes(n: number, headID: number, manager: number[], informTime: number[]): number {
    const adj: number[][] = new Array(n).fill(0).map(() => new Array());

    for (let i: number = 0; i < n; ++i) {
        const p: number = manager[i];
        if (p === -1) {
            continue;
        }
        adj[p].push(i);
    }

    let res: number = 0;

    const dfs = (id: number, acc: number): void => {
        if (adj[id].length === 0) {
            res = Math.max(res, acc);
            return;
        }

        for (const nei of adj[id]) {
            dfs(nei, acc + informTime[id]);
        }
    };

    dfs(headID, 0)

    return res;
};

const test = () => {
    const params = [
        {
            input: { n: 1, headID: 0, manager: [-1], informTime: [0] },
            output: 0,
        },
        {
            input: { n: 6, headID: 2, manager: [2,2,-1,2,2,2], informTime: [0,0,1,0,0,0] },
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const { n, headID, manager, informTime } = input;
        const result = numOfMinutes(n, headID, manager, informTime);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();