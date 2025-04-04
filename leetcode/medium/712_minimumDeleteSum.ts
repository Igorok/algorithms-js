function minimumDeleteSum(s1: string, s2: string): number {
    const n: number = s1.length;
    const m: number = s2.length;

    let sumOfCodes: number = 0;
    for (const char of s1) {
        sumOfCodes += char.charCodeAt(0);
    }
    for (const char of s2) {
        sumOfCodes += char.charCodeAt(0);
    }

    const substr = new Array(n).fill(0).map(() => new Array(m).fill(0));
    for (let i: number = 0; i < n; ++i) {
        for (let j: number = 0; j < m; ++j) {
            const top: number = (i > 0) ? substr[i-1][j] : 0;
            const left: number = (j > 0) ? substr[i][j-1] : 0;
            const diag: number = (i > 0 && j > 0) ? substr[i-1][j-1] : 0;

            substr[i][j] = Math.max(top, left);
            if (s1[i] === s2[j]) {
                substr[i][j] = Math.max(substr[i][j], diag + s1[i].charCodeAt(0));
            }
        }
    }

    return sumOfCodes - (substr[n-1][m-1] * 2);
};

/*

  3 3 4 1 1 2 8 9
1 0 0 0 1 1 1 1 1
1 0 0 0 1 2 2 2 2
2 0 0 0 1 2 3 3 3
6 0 0 0 1 2 3 3 3
3 1 1 1 1 2 3 3 3
5 1 1 1 1 2 3 3 3
3 1 2 2 2 2 3 3 3
4 1 2 3 3 3 3 3 3


*/

const test = () => {
    const params = [
        {
            input: ["sea", "eat"],
            output: 231,
        },
        {
            input: ["delete", "leet"],
            output: 403,
        },
    ];

    params.forEach(({input, output}) => {
        const [s1, s2]: string[] = input;
        const result = minimumDeleteSum(s1, s2);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

