function maxTotalFruits(fruits: number[][], startPos: number, k: number): number {
    const fruitsCount = new Array(1 + 2 * 10**5).fill(0);

    for (let [id, count] of fruits) {
        fruitsCount[id] = count;
    }

    for (let i: number = 1; i < fruitsCount.length; ++i) {
        fruitsCount[i] += fruitsCount[i-1];
    }

    let res: number = 0;

    for (let i: number = 0; i <= Math.floor(k / 2); ++i) {
        // left first
        let left: number = Math.max(startPos - i, 0);
        let right: number = Math.min(startPos + (k - i*2), fruitsCount.length - 1);
        let r: number = fruitsCount[right] - (left > 0 ? fruitsCount[left - 1] : 0);
        res = Math.max(res, r);

        // right first
        left = Math.max(0, startPos - (k - i*2));
        right = Math.min(startPos + i, fruitsCount.length - 1);
        r = fruitsCount[right] - (left > 0 ? fruitsCount[left - 1] : 0);
        res = Math.max(res, r);
    }

    return res;
};

/*
5

l l l l l s
          s r r r r r

    l l l s r
        l s r r r

        l s r r
      l l s r


*/

const test = () => {
    const params = [
        {
            input: {
                fruits: [[0,10000]],
                startPos: 200000,
                k: 200000,
            },
            output: 9,
        },
        {
            input: {
                fruits: [[2,8],[6,3],[8,6]],
                startPos: 5,
                k: 4,
            },
            output: 9,
        },
        {
            input: {
                fruits: [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]],
                startPos: 5,
                k: 4
            },
            output: 14,
        },
        {
            input: {
                fruits: [[0,3],[6,4],[8,5]],
                startPos: 3,
                k : 2,
            },
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const { fruits, startPos, k } = input;
        const result = maxTotalFruits(fruits, startPos, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();