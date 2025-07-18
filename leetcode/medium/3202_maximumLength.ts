function maximumLength_0(nums: number[], k: number): number {
    let res: number = 2;
    const length: number[][] = new Array(k).fill(0).map(() => new Array(k).fill(0));

    for (const num of nums) {
        const first: number = num % k;

        for (let remainder: number = k-1; remainder > -1; --remainder) {
            const second: number = (k + remainder - first) % k;

            if (!length[remainder][second]) {
                if (!length[remainder][first]) {
                    length[remainder][first] = 1;
                }

                continue;
            }

            length[remainder][first] = Math.max(
                length[remainder][first],
                length[remainder][second] + 1
            );


            if (!length[remainder][first]) {
                length[remainder][first] = 1;
            }

            res = Math.max(res, length[remainder][first]);
        }
    }

    return res;
};



function maximumLength(nums: number[], k: number): number {
    let res: number = 2;
    const length: number[][] = new Array(k).fill(0).map(() => new Array(k).fill(0));

    for (const num of nums) {
        const first: number = num % k;

        for (let remainder: number = k-1; remainder > -1; --remainder) {
            const second: number = (k + remainder - first) % k;

            if (!length[remainder][first]) {
                length[remainder][first] = 1;
                if (second === first) {
                    continue;
                }
            }

            if (!length[remainder][second]) {
                continue;
            }

            length[remainder][first] = Math.max(
                length[remainder][first],
                length[remainder][second] + 1
            );

            res = Math.max(res, length[remainder][first]);
        }
    }

    return res;
};
/*

nums: [1,2,3,4,5], k: 2
    1 2 3 4 5

  0 1
0 0 1
1 1 0

*/

const test = () => {
    const params = [
        {
            input: {
                nums: [1,4,2,3,1,4], k: 3,
            },
            output: 4,
        },
        {
            input: {
                nums: [1,2,3,4,5], k: 2,
            },
            output: 5,
        },

    ];

    params.forEach(({input, output}) => {
        const { nums, k } = input;
        const result = maximumLength(nums, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();