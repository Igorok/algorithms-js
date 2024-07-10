/**
 * intersectionOfTwoArrays
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    const first = new Set(nums1);
    const result = nums2.reduce((acc, val) => {
        if (!first.has(val)) return acc;

        acc.add(val);
        return acc;
    }, new Set());

    return Array.from(result.values());
};

const test = () => {
    const params = [
        {
            input: [[1,2,2,1], [2,2]],
            output: [2],
        },
        {
            input: [[4,9,5], [9,4,9,8,4]],
            output: [9,4],
        },
    ];

    params.forEach(({input, output}) => {
        const result = intersection(...input);

        console.log(
            JSON.stringify(result.sort()) === JSON.stringify(output.sort()) ? 'SUCCESS ' : 'ERROR ',
            'input', input,
            'output', output,
            'result', result,
        );

    });
};

test();
