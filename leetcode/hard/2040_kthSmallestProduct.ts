function kthSmallestProduct(nums1: number[], nums2: number[], k: number): number {
    const countProducts = (target: number) => {
        let count: number = 0;

        for (const num of nums1) {
            if (num === 0) {
                if (0 <= target) {
                    count += nums2.length;
                }
                continue;
            }

            let left: number = 0;
            let right: number = nums2.length - 1;
            let res: number = 0;

            while (left <= right) {
                const middle: number = Math.floor((left + right) / 2);

                if (num * nums2[middle] <= target) {
                    if (num < 0) {
                        right = middle - 1;
                        res = nums2.length - middle;
                    } else {
                        left = middle + 1;
                        res = middle + 1;
                    }
                } else {
                    if (num < 0) {
                        left = middle + 1;
                    } else {
                        right = middle - 1;
                    }
                }
            }

            count += res;
        }

        return count;
    }


    let left: number = -1 * 10**10;
    let right: number = 10**10;

    while (left <= right) {
        const product: number = Math.floor((left + right) / 2);
        const count: number = countProducts(product);

        if (count < k) {
            left = product + 1;
        } else {
            right = product - 1;
        }
    }

    return left;
};

/*

nums1: [-2,-1,0,1,2], nums2: [-3,-1,2,4,5], k: 3,
-2 * 5 = -10
-2 * 4 = -8
2 * -3 = -6
-1 * 5 = -5
-2 * 2 = -4
-1 * 4 = -4
1 * -3 = -3
2 * -1 = -2
-1 * 2 = -2
1 * -1 = -1
0 * -3 = 0
0 * -1 = 0
0 * 2 = 0
0 * 4 = 0
0 * 5 =  0
-1 * -1 = 1
-2 * -1 = 2
1 * 2 = 2
-1 * -3 = 3
1 * 4 = 4
2 * 2 = 4
1 * 5 = 5
-2 * -3 = 6
2 * 4 = 8
2 * 5 = 10

0
3, 3, 5, 2, 2 = 15
-1
3 3, 0, 2, 2 = 10



*/


const test = () => {
    const params = [
        {
            input: {
                nums1: [-2,-1,0,1,2], nums2: [-3,-1,2,4,5], k: 10,
            },
            output: -1,
        },

        {
            input: {
                nums1: [2,5], nums2: [3,4], k: 2,
            },
            output: 8,
        },
        {
            input: {
                nums1: [-4,-2,0,3], nums2: [2,4], k: 6,
            },
            output: 0,
        },
        {
            input: {
                nums1: [-2,-1,0,1,2], nums2: [-3,-1,2,4,5], k: 3,
            },
            output: -6,
        },

        {
            input: {
                nums1: [-2,-1,0,1,2], nums2: [-3,-1,2,4,5], k: 13,
            },
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums1, nums2, k } = input;
        const result = kthSmallestProduct(nums1, nums2, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

