function countLargestGroup(n: number): number {
    const getDigitSum = (num: number) => {
        let s: number = 0;
        while (num > 0) {
            s += num % 10;
            num = Math.floor(num / 10);
        }
        return s;
    };
    const groupSizeByDigitSum: Map<number, number> = new Map();
    let maxSize: number = 0;

    for (let i: number = 1; i <= n; ++i) {
        const s: number = getDigitSum(i);
        const size: number = (groupSizeByDigitSum.get(s) || 0) + 1;
        groupSizeByDigitSum.set(s, size);
        maxSize = Math.max(maxSize, size);
    }

    let res: number = 0;

    groupSizeByDigitSum.forEach((size: number) => {
        if (size === maxSize) {
            res += 1;
        }
    });

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                n: 13,
            },
            output: 4,
        },
        {
            input: {
                n: 2,
            },
            output: 2,
        },
    ];

    params.forEach(({input, output}) => {
        const { n } = input;

        const result = countLargestGroup(n);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();
