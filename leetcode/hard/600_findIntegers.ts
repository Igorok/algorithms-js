function findIntegers(n: number): number {
    const str: string = Number(n).toString(2);
    const memo: number[][][][][] = [];

    for (let i: number = 0; i < str.length; ++i) {
        memo.push([]);

        for (let j: number = 0; j < 2; ++j) {
            memo[i].push([]);

            for (let k: number = 0; k < 2; ++k) {
                memo[i][j].push([]);

                for (let l: number = 0; l < 2; ++l) {
                    memo[i][j][k].push([]);

                    for (let m: number = 0; m < 2; ++m) {
                        memo[i][j][k][l].push(-1);
                    }
                }
            }
        }
    }

    const rec = (id: number, boundary: boolean, zero: boolean, prev: number, isRepeat: boolean) => {
        if (id === str.length) {
            return isRepeat ? 0 : 1;
        }

        if (memo[id][boundary ? 1 : 0][zero ? 1 : 0][prev][isRepeat ? 1 : 0] !== -1) {
            return memo[id][boundary ? 1 : 0][zero ? 1 : 0][prev][isRepeat ? 1 : 0];
        }

        let res: number = 0;

        const upper: number = boundary ? Number(str[id]) : 1;

        for (let bit: number = 0; bit <= upper; ++bit) {
            if (zero && bit === 0) {
                res += rec(id + 1, false, true, 0, false);
                continue;
            }

            res += rec(
                id + 1,
                (boundary && bit === upper),
                (zero && bit === 0),
                bit,
                (isRepeat || (bit === 1 && bit === prev)),
            );
        }

        memo[id][boundary ? 1 : 0][zero ? 1 : 0][prev][isRepeat ? 1 : 0] = res;

        return res;
    }

    return rec(0, true, true, 0, false);
};

/*

10 - 1010
100 - 1100100
1000 - 1111101000


10- 1010
16 - 10000
161 - 10100001
1610 - 11001001010
1639 - 11001100111
16393 - 100000000001001

*/

const test = () => {
    const params = [
        {
            input: {
                n: 5
            },
            output: 5,
        },
        {
            input: {
                n: 1
            },
            output: 2,
        },
        {
            input: {
                n: 2
            },
            output: 3,
        },
        {
            input: {
                n: 5567
            },
            output: 610,
        },
    ];

    params.forEach(({input, output}) => {
        const { n } = input;
        const result = findIntegers(n);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();