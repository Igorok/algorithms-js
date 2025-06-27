function equationsPossible(equations: string[]): boolean {
    const parents: Map<string, string> = new Map();
    const counts: Map<string, number> = new Map();

    const getParent = (x: string): string => {
        const p: string | undefined = parents.get(x);
        if (!p) {
            parents.set(x, x);
            counts.set(x, 1);
            return x;
        }

        if (p === x) {
            return x;
        }

        const pOfp: string = getParent(p);
        parents.set(x, pOfp);

        return pOfp;
    };

    const setParent = (x: string, y: string): void => {
        const pX: string = getParent(x);
        const pY: string = getParent(y);

        if (pX === pY) {
            return;
        }

        const cX: number = counts.get(pX);
        const cY: number = counts.get(pY);

        if (cX < cY) {
            counts.set(pY, cX + cY);
            parents.set(pX, pY);
        } else {
            counts.set(pX, cX + cY);
            parents.set(pY, pX);
        }
    };

    for (let eq of equations) {
        const x: string = eq[0];
        const y: string = eq.at(-1);
        const condition: string = eq.slice(1, 3);

        if (condition === '==') {
            setParent(x, y)
        }
    }

    for (let eq of equations) {
        const x: string = eq[0];
        const y: string = eq.at(-1);
        const condition: string = eq.slice(1, 3);

        const pX: string = getParent(x);
        const pY: string = getParent(y);

        if (condition === '==' && pX !== pY) {
            return false;
        }
        if (condition === '!=' && pX === pY) {
            return false;
        }
    }

    return true;
};

const test = () => {
    const params = [
        {
            input: {
                equations: ["a==b","b!=a"],
            },
            output: false,
        },
        {
            input: {
                equations: ["b==a","a==b"],
            },
            output: true,
        },
    ];

    params.forEach(({input, output}) => {
        const { equations } = input;
        const result = equationsPossible(equations);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();