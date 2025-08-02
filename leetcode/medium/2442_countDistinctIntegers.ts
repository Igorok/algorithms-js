function countDistinctIntegers(nums: number[]): number {
    const res: Set<number> = new Set();

    const convert = (num: number) => {
        let res: number = 0;
        while ((num % 10) === 0) {
            num = num / 10;
        }
        while (num > 0) {
            const rem: number = num % 10;
            res *= 10;
            res += rem;
            num = Math.floor(num / 10);
        }
        return res;
    }

    for (const num of nums) {
        res.add(num);
        res.add(convert(num));
    }

    return res.size;
};

const test = () => {
    const params = [
        {
            input: {
                nums: [1,13,10,12,31],
            },
            output: 6,
        },
        {
            input: {
                nums: [2,2,2],
            },
            output: 1,
        },
    ];

    params.forEach(({ input, output }) => {
        const { nums } = input;
        const result = countDistinctIntegers(nums);

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
