/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    const memo = new Map();

    for (const num of nums) {
        memo.set(num, 0);
    }

    const getNext = (num) => {
        memo.set(num, 1);
        if (!memo.has(num+1)) {
            return 1;
        }
        return 1 + getNext(num+1);
    };
    const getPrev = (num) => {
        memo.set(num, 1);
        if (!memo.has(num-1)) {
            return 1;
        }
        return 1 + getPrev(num-1);
    };

    let res = 0;
    for (const num of nums) {
        if (memo.get(num) === 0) {
            const length = getPrev(num) + getNext(num) - 1;
            res = Math.max(res, length);
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: [100,4,200,1,3,2],
            output: 4,
        },
        {
            input: [0,3,7,2,5,8,4,6,0,1],
            output: 9,
        },
    ];

    params.forEach(({input, output}) => {
        const result = longestConsecutive(input);

        console.log(
            result === output ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();