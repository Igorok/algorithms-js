const mod: number = 7 + 10**9;

const powers: number[] = (() => {
    const length: number = 1 + 10**5;
    const powers: number[] = new Array(length).fill(1);

    for (let i: number = 1; i < length; ++i) {
        powers[i] = (powers[i-1] * 2) % mod;
    }

    return powers;
})();

function numSubseq(nums: number[], target: number): number {

    nums.sort((a: number, b: number) => a - b);

    const getIndex = (num: number, start: number) => {
        if (num >= nums.at(-1)) {
            return nums.length - 1;
        }

        let left: number = start;
        let right: number = nums.length - 1;
        let res: number = start;

        while (left <= right) {
            const middle: number = Math.floor((left + right) / 2);

            if (nums[middle] > num) {
                right = middle - 1;
            } else {
                res = middle;
                left = middle + 1;
            }
        }

        return res;
    }

    let res: number = 0;

    for (let start: number = 0; start < nums.length; ++start) {
        if (nums[start] * 2 > target) {
            break;
        }

        const end: number = getIndex(target - nums[start], start);
        res += powers[end - start];
        res %= mod;
    }

    return res;
};

/*

nums: [3,5,6,7], target: 9,
3 5 6

nums: [3,3,6,8], target: 10,

3; = 1
3, 3; = 3
3, 3, 6; = 1+1+1+1+1+1+1+1+1


1 2 3 4 5
1
1 2
1 2 3
1 - 3
1 2 3 4
1 2 - 4
1 - 3 4
1 - - 4
1 2 3 4 5
1 2 3 - 5
1 2 - 4 5





*/

const test = () => {
    const params = [
        {
            input: {
                nums: [3,5,6,7], target: 9,
            },
            output: 4,
        },
        {
            input: {
                nums: [3,3,6,8], target: 10,
            },
            output: 6,
        },
        {
            input: {
                nums: [2,3,3,4,6,7], target: 12,
            },
            output: 61,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums, target } = input;

        const result = numSubseq(nums, target);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();
