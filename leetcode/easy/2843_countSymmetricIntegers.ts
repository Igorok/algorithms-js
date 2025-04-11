function countSymmetricIntegers(low: number, high: number): number {
    let res: number = 0;

    const getStringSum = (str: string) => {
        let s: number = 0;
        for (const char of str) {
            s += Number(char);
        }
        return s;
    }

    const isSymmetric = (num: number) => {
        const strNum: string = String(num);
        if ((strNum.length % 2) === 1) {
            return false;
        }
        const middle: number = strNum.length / 2;

        return getStringSum(strNum.slice(0, middle)) === getStringSum(strNum.slice(middle))
    };

    for (let i = low; i <= high; ++i) {
        if (isSymmetric(i)) {
            res += 1;
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: [1, 100],
            output: 9,
        },
        {
            input: [1200, 1230],
            output: 4,
        },
    ];

    params.forEach(({input, output}) => {
        const nums = input as number[];

        const result = countSymmetricIntegers(nums[0], nums[1]);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();