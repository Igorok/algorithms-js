function numSimilarGroups(strs: string[]): number {
    type Node = {
        v: string,
        p: string,
        d: number,
    };
    const parents: Map<string, Node> = new Map();

    const getParent = (key: string): Node => {
        const parent: Node|undefined = parents.get(key);

        if (!parent) {
            const node: Node = { v: key, p: key, d: 1 };
            parents.set(key, node);
            return node;
        }

        if (parent.p === key) {
            return parent;
        }

        const parentOfParent: Node = getParent(parent.p);

        parent.p = parentOfParent.v;
        parents.set(parent.v, parent);

        return parentOfParent;
    };

    const setParent = (key1: string, key2: string): void => {
        const parent1: Node = getParent(key1);
        const parent2: Node = getParent(key2);

        if (parent1.v === parent2.v) {
            return;
        }

        if (parent1.d >= parent2.d) {
            parent1.d += parent2.d;
            parent2.p = parent1.v;
        } else {
            parent2.d += parent1.d;
            parent1.p = parent2.v;
        }
        parents.set(parent1.v, parent1);
        parents.set(parent2.v, parent2);
    };

    const isOk = (s1: string, s2: string): boolean => {
        let diff: number = 0;

        for (let i: number = 0; i < s1.length; ++i) {
            if (s1[i] !== s2[i]) {
                diff += 1;

                if (diff > 2) {
                    return false;
                }
            }
        }

        return true;
    };

    for (const s1 of strs) {
        for (const s2 of strs) {
            if (!isOk(s1, s2)) {
                continue;
            }

            setParent(s1, s2);
        }
    }

    const unique: Set<string> = new Set();

    for (const s of strs) {
        const parent: Node = getParent(s);
        unique.add(parent.p);
    }

    return unique.size;
};

const test = () => {
    const params = [
        {
            input: ["tars","rats","arts","star"],
            output: 2,
        },
        {
            input: ["omv","ovm"],
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const result = numSimilarGroups(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

