function findKthNumber(n: number, k: number): number {
    let res: number = 1;
    k -= 1;

    const getSteps = (left: number, right: number): number => {
        let steps: number = 0;

        while (left <= n) {
            steps += (Math.min(right, n + 1) - left);
            left *= 10;
            right *= 10;
        }

        return steps;
    };

    while (k > 0) {
        const steps = getSteps(res, res + 1);

        if (steps <= k) {
            res += 1;
            k -= steps;
        } else {
            res *= 10;
            k -= 1;
        }
    }

    return res;
};


const test = () => {
    const params = [
        {
            input: { n: 10, k: 8 },
            output: 7,
        },
        {
            input: { n: 19, k: 8 },
            output: 16,
        },
        {
            input: { n: 119, k: 50 },
            output: 36,
        },
        {
            input: { n: 13, k: 2 },
            output: 10,
        },
        {
            input: { n: 1, k: 1 },
            output: 1,
        },


        {
            input: { n: 111111, k: 5000 },
            output: 104497,
        },
    ];

    params.forEach(({input, output}) => {
        const { n, k } = input;
        const result = findKthNumber(n, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

