/*
const memo: Set<string> = new Set();
const getKey = (num: number): string => {
    const nums: number[] = new Array(10).fill(0);
    while (num > 0) {
        const r: number = num % 10;
        nums[r] += 1;
        num = Math.floor(num / 10);
    }
    return nums.join('_');
};

for (let i: number = 1; i <= 10**9; i *= 2) {
    memo.add(getKey(i));
}
console.log(JSON.stringify([...memo]));
*/

const memo: Set<string> = new Set(["0_1_0_0_0_0_0_0_0_0","0_0_1_0_0_0_0_0_0_0","0_0_0_0_1_0_0_0_0_0","0_0_0_0_0_0_0_0_1_0","0_1_0_0_0_0_1_0_0_0","0_0_1_1_0_0_0_0_0_0","0_0_0_0_1_0_1_0_0_0","0_1_1_0_0_0_0_0_1_0","0_0_1_0_0_1_1_0_0_0","0_1_1_0_0_1_0_0_0_0","1_1_1_0_1_0_0_0_0_0","1_0_1_0_1_0_0_0_1_0","1_0_0_0_1_0_1_0_0_1","0_1_1_0_0_0_0_0_1_1","0_1_0_1_1_0_1_0_1_0","0_0_1_1_0_0_1_1_1_0","0_0_0_1_0_2_2_0_0_0","1_2_1_1_0_0_0_1_0_0","0_1_2_0_2_0_1_0_0_0","0_0_2_0_1_1_0_0_2_0","1_1_0_0_1_1_1_1_1_0","1_1_2_0_0_1_0_1_0_1","1_1_0_1_3_0_0_0_0_1","1_0_0_1_0_0_1_0_4_0","0_2_1_0_0_0_2_3_0_0","0_0_1_3_2_2_0_0_0_0","1_1_0_0_1_0_2_1_2_0","0_2_2_1_1_0_0_2_1_0","0_0_1_1_2_2_2_0_1_0","1_1_1_1_0_1_1_1_1_1"]);

const getKey = (num: number): string => {
    const nums: number[] = new Array(10).fill(0);
    while (num > 0) {
        const r: number = num % 10;
        nums[r] += 1;
        num = Math.floor(num / 10);
    }
    return nums.join('_');
};

function reorderedPowerOf2(n: number): boolean {
    const key: string = getKey(n);
    return memo.has(key);
};

const test = () => {
    const params = [
        {
            input: {
                n: 1,
            },
            output: true,
        },
        {
            input: {
                n: 10,
            },
            output: false,
        },
    ];

    params.forEach(({input, output}) => {
        const { n } = input;
        const result = reorderedPowerOf2(n);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

