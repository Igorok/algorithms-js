function maxUncrossedLines(nums1: number[], nums2: number[]): number {
    const cache: number[][] = new Array(nums1.length).fill(0).map(() => new Array(nums2.length).fill(-1));

    const checkLines = (i: number, j: number) => {
        if (i === nums1.length || j === nums2.length) {
            return 0;
        }

        if (cache[i][j] !== -1) {
            return cache[i][j];
        }

        if (nums1[i] === nums2[j]) {
            const r: number = 1 + checkLines(i + 1, j + 1);
            cache[i][j] = r;
            return cache[i][j];
        }

        const r1: number = checkLines(i + 1, j + 1);
        const r2: number = checkLines(i, j + 1);
        const r3: number = checkLines(i + 1, j);

        cache[i][j] = Math.max(r1, r2, r3);

        return cache[i][j];
    };

    return checkLines(0, 0);
};

/*
2   5   1   2   5
10  5   2   1   5   2

1,2,3
5,5,5,2,3,4,4,1,2,3
*/

const test = () => {
    const params = [
        {
            input: { nums1: [1,4,2], nums2: [1,2,4] },
            output: 2,
        },
        {
            input: { nums1: [2,5,1,2,5], nums2: [10,5,2,1,5,2] },
            output: 3,
        },
        {
            input: { nums1: [1,3,7,1,7,5], nums2: [1,9,2,5,1] },
            output: 2,
        },
        {
            input: { nums1: [3,2,5,3,2,3,1,2,2,5,2,5,4,4,5], nums2: [3,2,3,3,5,5,1,3,3,1,5,2,5,5,3,2,4,2,1,2] },
            output: 10,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums1, nums2 } = input;

        const result = maxUncrossedLines(nums1, nums2);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();