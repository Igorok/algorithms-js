function subarraysWithKDistinct(nums: number[], k: number): number {
    let left: number = 0;
    const leftCount: Map<number, number> = new Map();
    let middle: number = 0;
    const middleCount: Map<number, number> = new Map();

    let res: number = 0;

    for (let right: number = 0; right < nums.length; ++right) {
        const cl: number = leftCount.get(nums[right]) || 0;
        leftCount.set(nums[right], cl + 1);

        const cm: number = middleCount.get(nums[right]) || 0;
        middleCount.set(nums[right], cm + 1);

        while (middleCount.size > k) {
            const c: number = middleCount.get(nums[middle]) - 1;

            if (c === 0) {
                middleCount.delete(nums[middle]);
            } else {
                middleCount.set(nums[middle], c);
            }

            middle += 1;
            left = middle;
        }


        while (middleCount.get(nums[middle]) > 1) {
            const cm: number = middleCount.get(nums[middle]);
            middleCount.set(nums[middle], cm - 1);
            middle += 1;
        }

        if (middleCount.size === k) {
            res += middle - left + 1;
        }
    }



    return res;
};

/*


1,2,2,2,2,2,1
11

1,2,2,2,1,2,2,1


*/

const test = () => {
    const params = [
        {
            input: {
                nums: [1,2,1,2,3], k: 2,
            },
            output: 7,
        },
        {
            input: {
                nums: [1,2,1,3,4], k: 3,
            },
            output: 3,
        },
        {
            input: {
                nums: [1,2,2,2,2,2,1], k: 2,
            },
            output: 11,
        },
        {
            input: {
                nums: [1,2,2,2,1,2,2,1], k: 2,
            },
            output: 24,
        },
        {
            input: {
                nums: [1,2,2,2,1,2,2,1], k: 1,
            },
            output: 12,
        },
    ];

    params.forEach(({ input, output }) => {
        const { nums, k } = input;
        const result = subarraysWithKDistinct(nums, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output)
                ? "SUCCESS "
                : "ERROR ",
            "input",
            JSON.stringify(input),
            "output",
            output,
            "result",
            result,
        );
    });
};

test();
