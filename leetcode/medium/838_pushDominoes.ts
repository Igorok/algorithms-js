function pushDominoes(dominoes: string): string {
    const res: string[] = new Array(dominoes.length).fill('.');

    let left: number = 0;
    for (let right = 0; right < dominoes.length; ++right) {
        if (dominoes[right] === 'L') {
            res[right] = 'L';
            if (dominoes[left] === 'L' || dominoes[left] === '.') {
                while (left < right) {
                    res[left] = 'L';
                    left += 1;
                }
                left = right;
                continue;
            }

            let l: number = left+1;
            let r: number = right-1;
            while (l < r) {
                res[l] = 'R';
                res[r] = 'L';
                l += 1;
                r -= 1;
            }
            left = right;
            continue;
        }

        if (dominoes[right] === 'R') {
            res[right] = 'R';
            if (dominoes[left] === 'L' || dominoes[left] === '.') {
                left = right;
                continue;
            }
            while (left < right) {
                res[left] = 'R';
                left += 1;
            }
            left = right;
            continue;
        }
    }

    if (left < dominoes.length && dominoes[left] === 'R') {
        while (left < dominoes.length) {
            res[left] = 'R';
            left += 1;
        }
    }

    return res.join('');
};

/*
.L.R.
LL.RR


*/


const test = () => {
    const params = [
        {
            input: { dominoes: ".L.R." },
            output: "LL.RR",
        },
        {
            input: { dominoes: "RR.L" },
            output: "RR.L",
        },
        {
            input: { dominoes: ".L.R...LR..L.." },
            output: "LL.RR.LLRRLL..",
        },
    ];

    params.forEach(({input, output}) => {
        const { dominoes } = input;
        const result = pushDominoes(dominoes);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();