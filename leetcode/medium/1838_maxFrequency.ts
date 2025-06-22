function maxFrequency(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);

    let res: number = 0;
    let left: number = 0;
    let sum: number = 0;

    for (let right: number = 0; right < nums.length; ++right) {
        sum += nums[right];
        let length: number = right - left + 1;

        while (sum + k < nums[right] * length) {
            sum -= nums[left];
            left += 1;
            length = right - left + 1;
        }

        res = Math.max(res, length);
    }

    return res;
};

/*

arr[right] * length < sum(arr[left], ..., arr[right])


*/

const test = () => {
    const params = [
        {
            input: {
                nums: [1,2,4], k: 5
            },
            output: 3,
        },
        {
            input: {
                nums: [1,4,8,13], k: 5
            },
            output: 2,
        },
        {
            input: {
                nums: [3,9,6], k: 2
            },
            output: 1,
        },
        {
            input: {
                nums: [1,1,1,1,5,6,7,7], k: 9
            },
            output: 5,
            // 9 - 1 - 2 -6
        },
    ];

    params.forEach(({input, output}) => {
        const { nums, k } = input;
        const result = maxFrequency(nums, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

