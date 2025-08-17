function findRedundantConnection(edges: number[][]): number[] {
    const parents: Map<number, number> = new Map();
    const childrenCount: Map<number, number> = new Map();

    const getParent = (num: number): number => {
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
    const setParent = (num1: number, num2: number): void => {
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

    let res: number[] = [];

    for (const [s, e] of edges) {
        const pS: number = getParent(s);
        const pE: number = getParent(e);

        if (pS === pE) {
            res = [s, e];
        }

        setParent(s, e);
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                edges: [[1,2],[1,3],[2,3]],
            },
            output: [2,3],
        },
        {
            input: {
                edges: [[1,2],[2,3],[3,4],[1,4],[1,5]],
            },
            output: [1,4],
        },
    ];

    params.forEach(({input, output}) => {
        const { edges } = input;
        const result = findRedundantConnection(edges);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

