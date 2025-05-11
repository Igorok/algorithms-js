function numTrees(n: number): number {
    const memo: number[] = new Array(n+1).fill(0);
    memo[0] = memo[1] = 1;

    for (let i: number = 2; i <= n; ++i) {
        for (let j = 0; j < i; ++j) {
            memo[i] += memo[j] * memo[i-j-1]
        }
    }

    return memo[n]
};


const test = () => {
    const params = [
        {
            input: 3,
            output: 5,
        },
        {
            input: 1,
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const result = numTrees(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();