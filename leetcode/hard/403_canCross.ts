function canCross(stones: number[]): boolean {
    if (stones[1] !== 1) {
        return false;
    }
    const shifts = [-1, 0 , 1];

    const getId = (start: number, val: number) => {
        let s: number = start;
        let e: number = stones.length - 1;
        let res: number = -1;

        while (s <= e) {
            const m: number = Math.floor((s + e) / 2);
            if (stones[m] === val) {
                return m;
            }

            if (stones[m] < val) {
                s = m + 1;
            } else {
                e = m - 1;
            }
        }

        return res;
    };


    const memo: Map<string, boolean> = new Map();

    const dfs = (id: number, unit: number) => {
        if (id === stones.length - 1) {
            return true;
        }

        const key: string = `${id}_${unit}`;
        if (memo.has(key)) {
            return memo.get(key);
        }

        let r: boolean = false;

        for (const shift of shifts) {
            const newUnit: number = unit + shift;
            const newId: number = getId(id, stones[id] + newUnit);
            if (id >= newId) {
                continue;
            }

            r = dfs(newId, newUnit);
            if (r) {
                break;
            }
        }

        memo.set(key, r);

        return r;
    };

    return dfs(1, 1);
};

const test = () => {
    const params = [
        {
            input: {
                stones: [0,1,3,5,6,8,12,17],
            },
            output: true,
        },
        {
            input: {
                stones: [0,1,2,3,4,8,9,11]
            },
            output: false,
        },
    ];

    params.forEach(({input, output}) => {
        const { stones } = input;
        const result = canCross(stones);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

