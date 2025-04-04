function numDistinct(s: string, t: string): number {
    const n: number = t.length;
    const m: number = s.length;

    const combinations: number[][] = new Array(n).fill(0).map(() => new Array(m).fill(0));
    const count: number[][] = new Array(n).fill(0).map(() => new Array(m).fill(0));

    for (let i: number = 0; i < n; ++i) {
        for (let j: number = 0; j < m; ++j) {
            const topCount: number = (i > 0) ? count[i-1][j] : 0;
            const leftCount: number = (j > 0) ? count[i][j-1] : 0;
            const diagCount: number = (i > 0 && j > 0) ? count[i-1][j-1] : 0;

            const leftComb: number = (j > 0) ? combinations[i][j-1] : 0;
            const diagComb: number = (i > 0 && j > 0) ? combinations[i-1][j-1] : 1;

            count[i][j] = Math.max(topCount, leftCount);
            combinations[i][j] = leftComb;

            if (t[i] === s[j]) {
                count[i][j] = Math.max(count[i][j], diagCount + 1);

                if (count[i][j] === i + 1) {
                    combinations[i][j] += diagComb;
                }
            }
        }
    }

    return combinations[n-1][m-1];
};


/*

  b a b g b a g
b 1 1 1 1 1 1 1
a 1 2 2 2 2 2 2
g 1 2 2 3 3 3 3

  b a b g b a g
b 1 1 2 2 3 3 3
a 0 1 1 1 1 4 4
g 0 0 0 1 1 1 5

---


  r a b b b i t
r 1 1 1 1 1 1 1
a 1 2 2 2 2 2 2
b 1 2 3 3 3 3 3
b 1 2 3 4 4 4 4
i 1 2 3 4 4 5 5
t 1 2 3 4 4 5 6

  r a b b b i t
r 1 1 1 1 1 1 1
a 0 1 1 1 1 1 1
b 0 0 1 2 3 3 3
b 0 0 0 1 3 3 3
i 0 0 0 0 0 3 3
t 0 0 0 0 0 0 3

*/

const test = () => {
    const params = [
        {
            input: ["babgbag", "bag"],
            output: 5,
        },
        {
            input: ["rabbbit", "rabbit"],
            output: 3,
        },
    ];

    params.forEach(({input, output}) => {
        const [s, t]: string[] = input;
        const result = numDistinct(s, t);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

