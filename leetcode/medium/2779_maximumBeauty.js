/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maximumBeauty_1 = function(nums, k) {
    const arr = nums.sort((a, b) => (a - b));
    let left = 0;
    let length = 0;
    let res = 0;
    for (let i = 0; i < arr.length; ++i) {
        let lMax = arr[left] + k;
        const rMin = Math.max(0, arr[i] - k);

        while (lMax < rMin) {
            left += 1;
            lMax = arr[left] + k;
        }
        length = (i - left) + 1;
        res = Math.max(res, length);
    }
    return res;
};

var maximumBeauty = function(nums, k) {
    const arr = nums.sort((a, b) => (a - b));
    const binSearchLess = (start, val) => {
        let s = start;
        let e = arr.length - 1;
        let r = e;
        while (s <= e) {
            const m = Math.round((s + e) / 2);
            if (arr[m] - k <= val) {
                r = m;
                s = m + 1;
            } else {
                e = m - 1;
            }
        }
        return r;
    };

    let left = 0;
    let right = 0;
    let length = 0;
    let res = 1;
    while (right < arr.length - 1) {
        right = binSearchLess(left, arr[left] + k);
        length = (right - left) + 1;
        res = Math.max(res, length);
        left += 1;
    }
    return res;
};

/*

[[4,6,1,2], 2]

1,2,4,6
0/ 0-3
3/ 4-8


*/


const test = () => {
    const params = [
        {
            input: [[4,6,1,2], 2],
            output: 3,
        },
        {
            input: [[1,1,1,1], 10],
            output: 4,
        },
        {
            input: [[1000], 0],
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const result = maximumBeauty(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();