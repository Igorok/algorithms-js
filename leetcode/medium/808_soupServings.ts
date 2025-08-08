function soupServings(n: number): number {
    const shifts: number[][] = [
        [100, 0], [75, 25], [50, 50], [25, 75],
    ];

    const memo: Map<string, number> = new Map();

    const dfs = (a: number, b: number, count: number): number => {
        if (a > 20_000) {
            return 1;
        }
        const key: string = `${a}_${b}`;

        if (memo.has(key)) {
            return memo.get(key);
        }

        let res: number = 0;

        for (const [as, bs] of shifts) {
            if ((a - as) <= 0 && (b - bs) <= 0) {
                res += 0.125;
                continue;
            }
            if ((a - as) <= 0) {
                res += 0.25;
                continue;
            }

            if (b-bs <= 0) {
                continue;
            }

            res += 0.25 * dfs((a-as), (b-bs), count+1);
        }

        // if ((count % 100) === 0) {
        //     console.log('count', count, 'res', res);
        // }


        memo.set(key, res);

        return res;
    };


    return dfs(n, n, 0);
};


/*

10**9 / 25 = 40_000_000

A - 100; B - 0;
A - 75; B - 25;
A - 50; B - 50;
A - 25; B - 75;

---

n: 50,
(0.25 + 0.25) + (0.25/2) = 0.625

---

n: 100,
(0.25 + 3*0.0625 + 2*0.0625 + 1*0.0625)+(0.0625+0.0625+0.0625)/2 = 0.71875

        0.25; [0, 100]
                        0.0625; [0, 100]
100     0.25; [25, 75]  0.0625; [0,  50]
                        0.0625; [0,  25]
                        0.0625; [0,   0]

                        0.0625; [0, 50]
        0.25; [50, 50]  0.0625; [0, 25]
                        0.0625; [0,  0]
                        0.0625; [25, 0]

                        0.0625; [0, 25]
        0.25; [75, 25]  0.0625; [0,  0]
                        0.0625; [25, 0]
                        0.0625; [50, 0]

*/

const test = () => {
    const params = [
        {
            input: {
                n: 50,
            },
            output: 0.62500,
        },
        {
            input: {
                n: 100,
            },
            output: 0.71875,
        },
        {
            input: {
                n: 20000,
            },
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const { n } = input;
        const result = soupServings(n);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();