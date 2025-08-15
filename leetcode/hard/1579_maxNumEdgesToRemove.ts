function maxNumEdgesToRemove(n: number, edges: number[][]): number {
    const getRemoved = (type: number) => {
        const parents: Map<number, number> = new Map();
        const childrenCount: Map<number, number> = new Map();
        let common: number = 0;
        let removed: number = 0;

        const getParent = (num: number) => {
            if (!parents.has(num)) {
                parents.set(num, num);
                childrenCount.set(num, 1);
                return num;
            }

            const parent: number = parents.get(num);
            if (parent === num) {
                return num;
            }

            const grandParent: number = getParent(parent);

            if (parent !== grandParent) {
                parents.set(num, grandParent);
            }

            return grandParent;
        };

        const setParent = (num1: number, num2: number) => {
            const parent1: number = getParent(num1);
            const parent2: number = getParent(num2);

            if (parent1 === parent2) {
                return;
            }

            const count1: number = childrenCount.get(parent1);
            const count2: number = childrenCount.get(parent2);

            if (count1 < count2) {
                parents.set(parent1, parent2);
                childrenCount.set(parent2, count1 + count2);
            } else {
                parents.set(parent2, parent1);
                childrenCount.set(parent1, count1 + count2);
            }
        };

        for (const [t, s, e] of edges) {
            if (t !== 3) continue;

            const pS: number = getParent(s);
            const pE: number = getParent(e);
            if (pS === pE) {
                common += 1;
                continue;
            }

            setParent(s, e);
        }

        for (const [t, s, e] of edges) {
            if (t !== type) continue;

            const pS: number = getParent(s);
            const pE: number = getParent(e);
            if (pS === pE) {
                removed += 1;
                continue;
            }

            setParent(s, e);
        }

        const p: number = getParent(edges[0][1]);
        if (childrenCount.get(p) < n) {
            return [-1, -1];
        }

        return [common, removed];
    };

    const a: number[] = getRemoved(1);
    if (a[0] === -1) {
        return -1;
    }
    const b: number[] = getRemoved(2);
    if (b[0] === -1) {
        return -1;
    }


    return a[1] + b[1] + a[0];
};

const test = () => {
    const params = [
        {
            input: {
                n: 4, edges: [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]],
            },
            output: 2,
        },
        {
            input: {
                n: 4, edges: [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
            },
            output: 0,
        },
        {
            input: {
                n: 4, edges: [[3,2,3],[1,1,2],[2,3,4]]
            },
            output: -1,
        },
        {
            input: {
                n: 13, edges: [[1,1,2],[2,1,3],[3,2,4],[3,2,5],[1,2,6],[3,6,7],[3,7,8],[3,6,9],[3,4,10],[2,3,11],[1,5,12],[3,3,13],[2,1,10],[2,6,11],[3,5,13],[1,9,12],[1,6,8],[3,6,13],[2,1,4],[1,1,13],[2,9,10],[2,1,6],[2,10,13],[2,2,9],[3,4,12],[2,4,7],[1,1,10],[1,3,7],[1,7,11],[3,3,12],[2,4,8],[3,8,9],[1,9,13],[2,4,10],[1,6,9],[3,10,13],[1,7,10],[1,1,11],[2,4,9],[3,5,11],[3,2,6],[2,1,5],[2,5,11],[2,1,7],[2,3,8],[2,8,9],[3,4,13],[3,3,8],[3,3,11],[2,9,11],[3,1,8],[2,1,8],[3,8,13],[2,10,11],[3,1,5],[1,10,11],[1,7,12],[2,3,5],[3,1,13],[2,4,11],[2,3,9],[2,6,9],[2,1,13],[3,1,12],[2,7,8],[2,5,6],[3,1,9],[1,5,10],[3,2,13],[2,3,6],[2,2,10],[3,4,11],[1,4,13],[3,5,10],[1,4,10],[1,1,8],[3,3,4],[2,4,6],[2,7,11],[2,7,10],[2,3,12],[3,7,11],[3,9,10],[2,11,13],[1,1,12],[2,10,12],[1,7,13],[1,4,11],[2,4,5],[1,3,10],[2,12,13],[3,3,10],[1,6,12],[3,6,10],[1,3,4],[2,7,9],[1,3,11],[2,2,8],[1,2,8],[1,11,13],[1,2,13],[2,2,6],[1,4,6],[1,6,11],[3,1,2],[1,1,3],[2,11,12],[3,2,11],[1,9,10],[2,6,12],[3,1,7],[1,4,9],[1,10,12],[2,6,13],[2,2,12],[2,1,11],[2,5,9],[1,3,8],[1,7,8],[1,2,12],[1,5,11],[2,7,12],[3,1,11],[3,9,12],[3,2,9],[3,10,11]],
            },
            output: 114,
        },
    ];

    params.forEach(({input, output}) => {
        const { n, edges } = input;
        const result = maxNumEdgesToRemove(n, edges);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

