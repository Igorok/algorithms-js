function numDupDigitsAtMostN(n: number): number {
    const str: string = String(n);
    const memo: number[][][][][] = [];
    for (let i: number = 0; i < str.length; ++i) {
        memo.push([]);

        for (let j: number = 0; j < 2; ++j) {
            memo[i].push([]);

            for (let k: number = 0; k < 2; ++k) {
                memo[i][j].push([]);

                const limit: number = 2 ** 10;
                for (let l: number = 0; l <= limit; ++l) {
                    memo[i][j][k].push([]);

                    for (let m: number = 0; m < 2; ++m) {
                        memo[i][j][k][l].push(-1);
                    }
                }
            }
        }
    }

    const rec = (id: number, zero: boolean, boundary: boolean, mask: number, isRepeat: boolean) => {
        if (id === str.length) return isRepeat ? 1 : 0;

        const v: number = memo[id][zero ? 1 : 0][boundary ? 1 : 0][mask][isRepeat ? 1 : 0];
        if (v !== -1) return v;

        let res: number = 0;
        const upper: number = boundary ? Number(str[id]) : 9;

        for (let i: number = 0; i <= upper; ++i) {

            if (i === 0 && zero) {
                res += rec(id + 1, true, false, 0, false);
                continue;
            }

            let z: boolean = zero;
            if (i !== 0) {
                z = false;
            }
            const b: boolean = (i === upper && boundary);
            const m: number = mask | (1 << i);
            const isRep: boolean = isRepeat || ((mask & (1 << i)) > 0);

            res += rec(id + 1, z, b, m, isRep);
        }

        memo[id][zero ? 1 : 0][boundary ? 1 : 0][mask][isRepeat ? 1 : 0] = res;

        return res;
    };




    return rec(0, true, true, 0, false);

};


const test = () => {
    const params = [
        {
            input: {
                n: 20
            },
            output: 1,
        },
        {
            input: {
                n: 100
            },
            output: 10,
        },
        {
            input: {
                n: 1000
            },
            output: 262,
        },
    ];

    params.forEach(({input, output}) => {
        const { n } = input;
        const result = numDupDigitsAtMostN(n);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();