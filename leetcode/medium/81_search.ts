function search(nums: number[], target: number): boolean {

    const getPivot = () => {
        if (nums[0] < nums.at(-1) || nums.length === 1) {
            return 0;
        }

        let left: number = 0;
        let right: number = nums.length - 1;

        while (left <= right) {
            const middle: number = Math.floor((left + right) / 2);

            if (
                (middle === nums.length - 1 && nums[middle - 1] > nums[middle]) ||
                (middle - 1 > -1 && middle + 1 < nums.length && nums[middle - 1] > nums[middle] && nums[middle + 1] <= nums[middle])
            ) {
                return middle;
            }

            if (middle + 1 < nums.length && nums[middle] > nums[middle + 1]) {
                return middle + 1;
            }

            if (right + 1 < nums.length && nums[right] > nums[right + 1]) {
                return right + 1;
            }

            if (nums[middle] < nums[left] && nums[middle] < nums[right] && nums[left] > nums[right]) {
                right = middle - 1;
                continue;
            }

            if (nums[middle] > nums[left] && nums[middle] > nums[right]) {
                left = middle + 1;
                continue;
            }

            const mLeft: number = Math.floor((left + middle) / 2);
            const mRight: number = Math.floor((middle + right) / 2);

            if (nums[middle] < nums[mLeft] && nums[middle] < nums[mRight] && nums[mLeft] > nums[mRight]) {
                right = middle - 1;
                continue;
            }
            if (nums[middle] > nums[mLeft] && nums[middle] > nums[mRight]) {
                left = middle + 1;
                continue;
            }


            right -= 1;
        }

        return 0;
    }

    const pivot: number = getPivot();


    const isExists = (start: number, end: number): boolean => {
        let left: number = start;
        let right: number = end;

        while (left <= right) {
            const middle: number = Math.floor((left + right) / 2);
            if (nums[middle] === target) {
                return true;
            }

            if (target > nums[middle]) {
                left = middle + 1;
            } else {
                right = middle - 1;
            }
        }

        return false;
    };


    return (
        isExists(0, pivot) ||
        isExists(pivot, nums.length - 1)
    );
};

/*

4,4,4, 5,5,5, 6,6,6, 1,1,1 2,2,2 3,3,3


nums[middle] < nums[left] && nums[middle] < nums[right] && nums[left] > nums[right]
right = middle - 1

nums[middle] > nums[left] && nums[middle] > nums[right]
left = middle + 1



0 1 1


*/

const test = () => {
    const params = [
        {
            input: {
                nums: [4,5,6,7,0,1,2], target: 0,
            },
            output: true,
        },
        {
            input: {
                nums: [1,0,1,1,1], target: 0,
            },
            output: true,
        },
        {
            input: {
                nums: [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], target: 2,
            },
            output: true,
        },
        {
            input: {
                nums: [1], target: 0,
            },
            output: false,
        },
        {
            input: {
                nums: [2,5,6,0,0,1,2], target: 0,
            },
            output: true,
        },
        {
            input: {
                nums: [2,5,6,0,0,1,2], target: 3
            },
            output: false,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums, target } = input;
        const result = search(nums, target);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();