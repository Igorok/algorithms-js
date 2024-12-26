/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var findTargetSumWays_0 = function(nums, target) {
    let res = 0;

    const rec = (id, sum) => {
        if (id === nums.length) {
            if (sum === target) {
                res += 1;
            }
            return;
        }

        rec(id + 1, sum + nums[id]);
        rec(id + 1, sum - nums[id]);
    };

    rec(0, 0);

    return res;
};

var findTargetSumWays = function(nums, target) {
    const cache = new Map();
    const rec = (id, sum) => {
        const key = [id, sum].join('_');
        let r = cache.get(key);
        if (r !== undefined) {
            return r;
        }

        if (id === nums.length) {
            return (sum === target) ? 1 : 0;
        }

        r = rec(id + 1, sum + nums[id]) + rec(id + 1, sum - nums[id]);
        cache.set(key, r);

        return r;
    };

    const res = rec(0, 0);

    return res;
};


const test = () => {
    const params = [
        {
            input: [[1,1,1,1,1], 3],
            output: 5,
        },
        {
            input: [[1], 1],
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const result = findTargetSumWays(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();