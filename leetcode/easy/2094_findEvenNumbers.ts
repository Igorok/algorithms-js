
function findEvenNumbers(digits: number[]): number[] {
    const digitCount: Map<number, number> = new Map();
    for (const digit of digits) {
        const count: number = digitCount.get(digit) || 0;
        digitCount.set(digit, count + 1);
    }

    let res: number[] = [];

    for (let i: number = 100; i < 999; i += 2) {
        const cntMap: Map<number, number> = new Map();
        let n: number = i;
        while (n > 0) {
            const r: number = n % 10;
            const cnt: number = cntMap.get(r) || 0;
            cntMap.set(r, cnt + 1);
            n = Math.floor(n / 10);
        }

        let ok: boolean = true;
        cntMap.forEach((val: number, key: number) => {
            const cnt: number = digitCount.get(key) || 0;
            if (cnt < val) {
                ok = false;
                return;
            }
        });
        if (ok) {
            res.push(i);
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: { digits: [2,1,3,0] },
            output: [102,120,130,132,210,230,302,310,312,320],
        },
        {
            input: { digits: [2,2,8,8,2] },
            output: [222,228,282,288,822,828,882],
        },
        {
            input: { digits: [3,7,5] },
            output: [],
        },
    ];

    params.forEach(({input, output}) => {
        const { digits } = input;

        const result = findEvenNumbers(digits);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();