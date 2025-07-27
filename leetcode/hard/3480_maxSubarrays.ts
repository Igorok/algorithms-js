function maxSubarrays(n: number, conflictingPairs: number[][]): number {
    const leftBorders: number[][] = new Array(n+1).fill(0).map(() => []);
    for (const arr of conflictingPairs) {
        const l: number = Math.min(...arr);
        const r: number = Math.max(...arr);
        leftBorders[r].push(l);
    }

    const lastBorders: number[] = [0, 0];

    let res: number = 0;
    let profit: number = 0;
    const profitBorders = new Array(n+1).fill(0);

    for (let right: number = 1; right <= n; ++right) {
        for (const l of leftBorders[right]) {
            if (l > lastBorders[1]) {
                lastBorders[0] = lastBorders[1];
                lastBorders[1] = l;
            } else if (l > lastBorders[0]) {
                lastBorders[0] = l;
            }
        }

        const available: number = right - lastBorders[1];
        res += available;

        const diff: number = lastBorders[1]-lastBorders[0];
        profitBorders[lastBorders[1]] += diff;

        profit = Math.max(profit, profitBorders[lastBorders[1]]);
    }

    return res + profit;
};


/*

n: 5,
conflictingPairs: [[1,2],[2,5],[3,5]],

5*6/2=15

1 2 3 4 5
1 x x x x   1;      + 1,2; 1,2,3; 1,2,3,4;
- 2 3 4 x   2; 2,3; 2,3,4;      +
- - 3 4 x   3; 3,4;     + 3,4,5;
- - - 4 5   4; 4,5;
- - - - 5   5;

1+3+2+2+1= 9;

0 1 2 3 4 5
0 1 - -



*/

const test = () => {
    const params = [
        {
            input: {
                n: 5,
                conflictingPairs: [[1,2],[2,5],[3,5]],
            },
            output: 12,
        },
        {
            input: {
                n: 4,
                conflictingPairs: [[2,3],[1,4]],
            },
            output: 9,
        },
    ];

    params.forEach(({ input, output }) => {
        const { n, conflictingPairs } = input;
        const result = maxSubarrays(n, conflictingPairs);

        console.log(
            JSON.stringify(result) === JSON.stringify(output)
                ? "SUCCESS "
                : "ERROR ",
            "input",
            JSON.stringify(input),
            "output",
            output,
            "result",
            result,
        );
    });
};

test();
