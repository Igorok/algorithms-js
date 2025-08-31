class TreeAncestor {
    parentsList: number[][] = [];
    deeps: number[] = [];

    constructor(n: number, parent: number[]) {
        const adj: number[][] = new Array(n).fill(0).map(() => []);
        for (let i: number = 0; i < parent.length; ++i) {
            if (i === 0) continue;
            adj[parent[i]].push(i);
        }

        this.deeps = new Array(n).fill(0);
        this.parentsList = new Array(n).fill(0).map(() => []);

        const dfs = (node: number, anc: number) => {
            this.parentsList[node].push(anc);

            if (node !== 0) {
                this.deeps[node] = this.deeps[anc] + 1;

                let i: number = 1;
                let p: number = this.parentsList[node][i-1];
                while (Number.isFinite(this.parentsList[p][i-1]) && this.parentsList[p][i-1] !== -1) {
                    this.parentsList[node].push(
                        this.parentsList[p][i-1]
                    );

                    i += 1;
                    p = this.parentsList[node][i-1];
                }
            }

            for (const nei of adj[node]) {
                dfs(nei, node);
            }
        }

        dfs(0, -1)

    }

    getKthAncestor(node: number, k: number): number {
        if (this.deeps[node] < k) return -1;

        const l: number = Math.ceil(Math.log2(k));
        let n: number = node;

        for (let i: number = 0; i <= l; ++i) {
            const bit: number = (1 << i) & k;
            if (bit !== 0) {
                n = this.parentsList[n][i];
            }
        }

        return n;
    }
}

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * var obj = new TreeAncestor(n, parent)
 * var param_1 = obj.getKthAncestor(node,k)
 */



/*

[
0,[0,],
1,[0,],
2,[0,],
3,[1,0],
4,[1,0],
5,[2,0],
6,[2,0],
7,[3,1],
8,[3,1],
9,[7,3,0],
10,[7,3,0],
]

100
101


*/

const test = () => {
    const params = [
        {
            input: {
                n: 4,
                parent: [-1,2,3,0],
                queries: [[2,3],[2,2],[2,1]],
            },
            output: [-1,0,3],
        },
        {
            input: {
                n: 7,
                parent: [-1, 0, 0, 1, 1, 2, 2],
                queries: [[3, 1], [5, 2], [6, 3]],
            },
            output: [1, 0, -1],
        },
    ];

    params.forEach(({input, output}) => {
        const { n, parent, queries } = input;
        const ta = new TreeAncestor(n, parent);

        for (let i: number = 0; i < queries.length; ++i) {
            const [node, k] = queries[i];
            const result: number = ta.getKthAncestor(node, k);

            console.log(
                JSON.stringify(result) === JSON.stringify(output[i]) ? 'SUCCESS ' : 'ERROR ',
                'input', node, k,
                'output', output[i],
                'result', result,
            );
        }

    });
};

test();