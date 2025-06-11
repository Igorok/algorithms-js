function maxDifference(s: string, k: number): number {
    const chars: string[] = ['0', '1', '2', '3', '4'];
    let res: number = Number.MIN_SAFE_INTEGER;

    const getKey = (count1: number, count2: number): number => ((count1 & 1) << 1) | (count2 & 1);

    for (const char1 of chars) {
        for (const char2 of chars) {
            if (char1 === char2) {
                continue;
            }

            let current1: number = 0;
            let current2: number = 0;
            let prev1: number = 0;
            let prev2: number = 0;
            let left: number = -1;

            const minDiffs = new Array(4).fill(Number.MAX_SAFE_INTEGER);

            for (let right: number = 0; right < s.length; ++right) {
                if (s[right] === char1) {
                    current1 += 1;
                }
                if (s[right] === char2) {
                    current2 += 1;
                }

                while (right - left >= k && current2 - prev2 > 1) {
                    if (s[left] === char1) {
                        prev1 += 1;
                    }
                    if (s[left] === char2) {
                        prev2 += 1;
                    }

                    const key: number = getKey(prev1, prev2);
                    const leftDiff: number = prev1 - prev2;

                    minDiffs[key] = Math.min(minDiffs[key], leftDiff);

                    left += 1;
                }

                const rightKey: number = getKey(current1, current2);
                const leftKey: number = rightKey ^ 2;
                const rightDiff: number = current1 - current2;

                if (minDiffs[leftKey] !== Number.MAX_SAFE_INTEGER) {
                    res = Math.max(
                        res,
                        rightDiff - minDiffs[leftKey]
                    );
                }
            }

        }
    }



    return res;
};

/*

diff = countOdd - countEven
countA = prefix[odd1] - prefix[odd0]
countB = prefix[even1] - prefix[even0]
diff = (prefix[odd1] - prefix[odd0]) - (prefix[even1] - prefix[even0])
    = prefix[odd1] - prefix[odd0] - prefix[even1] + prefix[even0]
    = (prefix[odd1] - prefix[even1]) - (prefix[odd0] - prefix[even0])

odd_even = ?
odd - even = odd; 1 ^ 0 = 1;
even - odd = odd; 0 ^ 1 = 1;
odd - odd = even; 0 ^ 0 = 0;
even - even = even; 1 ^ 1 = 0;

comb0 ^ comb1 = 10
comb1 = comb0 ^ 10

res = max(res, diff[comb0] - diff[comb0 ^ 10])





*/


/*

111233334444444
11123333444444411111111


*/

const test = () => {
    const params = [
        {
            input: {
                s: '12233', k: 4,
            },
            output: -1,
        },
        {
            input: {
                s: '1122211', k: 3,
            },
            output: 1,
        },
        {
            input: {
                s: '110', k: 3,
            },
            output: -1,
        },
        {
            input: {
                s: '111233334444444', k: 4,
            },
            output: 5,
        },
        {
            input: {
                s: '11123333444444411111111', k: 4,
            },
            output: 7,
        },
    ];

    params.forEach(({input, output}) => {
        const {s, k } = input;
        const result = maxDifference(s, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

