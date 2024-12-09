/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var isArraySpecial_1 = function(nums, queries) {
    const isSpecial = (start, end) => {
        let rem = (nums[start] % 2);
        for (let i = start + 1; i <= end; ++i) {
            const r = (nums[i] % 2);
            if (r === rem) {
                return false;
            }
            rem = r;
        }
        return true;
    };

    const res = [];
    for (const [s, e] of queries) {
        res.push(isSpecial(s, e));
    }

    return res;
};

var isArraySpecial = function(nums, queries) {
    const prefixSum = new Array(nums.length).fill(0);
    prefixSum[0] = 1

    let remainder = (nums[0] % 2);
    for (let i = 1; i < nums.length; ++i) {
        const r = (nums[i] % 2);
        prefixSum[i] = (remainder === r) ? 1 : prefixSum[i-1] + 1;
        remainder = r;
    }

    return queries.map(([s, e]) => ((e - s) === (prefixSum[e] - prefixSum[s])));
};



const test = () => {
    const params = [
        {
            input: [[3,4,1,2,6], [[0,4]]],
            output: [false],
        },
        {
            input: [[4,3,1,6], [[0,2],[2,3]]],
            output: [false,true],
        },
    ];

    params.forEach(({input, output}) => {
        const result = isArraySpecial(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();