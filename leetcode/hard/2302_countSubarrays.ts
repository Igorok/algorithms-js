function countSubarraysBf(nums: number[], k: number): number {
    let res: number = 0;

    for (let i: number = 0; i < nums.length; ++i) {
        let sum: number = 0;
        for (let j: number = i; j < nums.length; ++j) {
            sum += nums[j];
            if ((j - i + 1) * sum < k) {
                res += 1;
            }
        }
    }

    return res;
};


function countSubarrays(nums: number[], k: number): number {
    let res: number = 0;

    let sum: number = 0;
    let left: number = 0;
    for (let right: number = 0; right < nums.length; ++right) {
        sum += nums[right];
        let length: number = right - left + 1;
        let product: number = length * sum;

        while (product >= k) {
            sum -= nums[left];
            left += 1;
            length = right - left + 1;
            product = length * sum;
        }

        res += length;
    }

    return res;
};

/*
nums: [2,1,4,3,5], k: 10
2   2*1 = 2; res = 0+ (0-0+1) = 1
1   (2+1)*2 = 6; res = 1 + (1 - 0 + 1) = 3
4   (2+1+4)*3 = 21; (1+4)*2=10; 4*1=8; res = 3 + (2-2+1) = 4
3
5


nums: [1,2,3,4,5,6,7,8,9,10], k: 20



*/

const test = () => {

    const params = [
        {
            input: { nums: [2,1,4,3,5], k: 10 },
            output: 6,
        },
        {
            input: { nums: [1,1,1], k: 5 },
            output: 5,
        },
        {
            input: { nums: [1,2,3,4,5,6,7,8,9,10], k: 20 },
            output: 15,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums, k } = input;

        const result = countSubarrays(nums, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();