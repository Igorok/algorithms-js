function maxDistance(s: string, k: number): number {
    const count = {
        'N': 0,
        'S': 0,
        'W': 0,
        'E': 0,
    };

    const getChanged = (loc1: number, loc2: number, limit: number): number[] => {
        let x1: number = loc1;
        let x2: number = loc2;
        let l: number = limit;

        if (x2 > 0 && l > 0) {
            if (l >= x2) {
                l -= x2;
                x1 += x2
                x2 = 0;
            } else {
                x2 -= l;
                x1 += l;
                l = 0;
            }
        }

        return [x1-x2, l];
    };

    let res: number = 0;
    for (const char of s) {
        count[char] += 1;


        // y
        let [y1, y2] = count.S > count.N ? [count.S, count.N] : [count.N, count.S];
        const [y, limit] = getChanged(y1, y2, k);

        // x
        let [x1, x2] = count.E > count.W ? [count.E, count.W] : [count.W, count.E];
        const [x, l] = getChanged(x1, x2, limit);

        const r: number = x + y;
        res = Math.max(r, res);
    }

    return res;
};

/*

Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.

NWSE
N 1
S 1
W 1
E 1


*/

const test = () => {
    const params = [

        {
            input: {
                s: "NWSE", k: 1
            },
            output: 3,
        },
        {
            input: {
                s: "NSWWEW", k: 3
            },
            output: 6,
        },

        {
            input: {
                s: "EWWE", k: 0
            },
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const { s, k } = input;
        const result = maxDistance(s, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();