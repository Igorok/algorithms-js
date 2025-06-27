function longestSubsequence_0(s: string, k: number): number {
    let res: number = 0;

    const rec = (memo: string, id: number): void => {
        const num: number = parseInt(memo, 2);
        if (num > k) {
            return;
        }

        res = Math.max(res, memo.length);

        if (id === s.length) {
            return;
        }

        rec(memo, id + 1);
        rec(memo + s[id], id + 1);
    }

    rec('', 0);

    return res;
};

function longestSubsequence(s: string, k: number): number {
    const tpl: number[] = new Array(s.length).fill(0);
    let res: number = 0;

    for (let i: number = s.length - 1; i > -1; --i) {
        if (s[i] === '0') {
            res += 1;
            continue;
        }

        tpl[i] = 1;
        const num: number = parseInt(tpl.join(''), 2);
        if (num > k) {
            tpl[i] = 0
        } else {
            res += 1;
        }
    }

    return res;
};

/*

s: "1001010", k: 5,
0101001
010-00
0-0-00

---

00101001
00-0-001


*/

const test = () => {
    const params = [
        {
            input: {
                s: "1001010", k: 5,
            },
            output: 5,
        },
        {
            input: {
                s: "00101001", k: 1,
            },
            output: 6,
        },
        {
            input: {
                s: "001010101011010100010101101010010", k: 93951055,
            },
            output: 6,
        },
    ];

    params.forEach(({input, output}) => {
        const { s, k } = input;
        const result = longestSubsequence(s, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();