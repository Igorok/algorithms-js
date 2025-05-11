function countBalancedPermutations(num: string): number {
    let sum: number = num.split('').reduce((acc, cur) => acc + Number(cur), 0);
    if ((sum % 2) === 1) {
        return 0;
    }

    


    return 0;
};

const test = () => {
    const params = [
        {
            input: { num: "123" },
            output: 2,
        },
        {
            input: { num: "112" },
            output: 1,
        },
        {
            input: { num: "12345" },
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const { num } = input;

        const result = countBalancedPermutations(num);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();