function minInsertions(s: string): number {
    const reversed: string = s.split('').reverse().join('');
    const memo: number[][] = new Array(s.length).fill(0).map(() => new Array(s.length).fill(0));

    for (let i: number = 0; i < s.length; ++i) {
        for (let j: number = 0; j < s.length; ++j) {
            const top: number = i > 0 ? memo[i-1][j] : 0;
            const left: number = j > 0 ? memo[i][j-1] : 0;
            const diag: number = (i > 0 && j > 0) ? memo[i-1][j-1] : 0;

            memo[i][j] = Math.max(top, left);
            if (s[i] === reversed[j]) {
                memo[i][j] = Math.max(memo[i][j], diag + 1);
            }
        }
    }

    return s.length - memo.at(-1).at(-1);
};

/*

leetcode
leedtcoctdeel

mbadm
mbdadbm

abcdad
abcdadcba

  z z a z z
z 1 1 1 1 1
z 1 2 2 2 2
a 1 2 3 3 3
z 1 2 3 4 4
z 1 2 3 4 5

*/

const test = () => {
    const params = [
        {
            input: { s: "zzazz" },
            output: 0,
        },
        {
            input: { s: "mbadm" },
            output: 2,
        },
        {
            input: { s: "leetcode" },
            output: 5,
        },
    ];

    params.forEach(({input, output}) => {
        const { s } = input;

        const result = minInsertions(s);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();