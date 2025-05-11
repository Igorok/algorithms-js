function minSum(nums1: number[], nums2: number[]): number {
    let s1: number = 0;
    let s2: number = 0;
    let z1: number = 0;
    let z2: number = 0;

    for (const num of nums1) {
        if (num === 0) {
            z1 += 1;
        } else {
            s1 += num;
        }
    }
    for (const num of nums2) {
        if (num === 0) {
            z2 += 1;
        } else {
            s2 += num;
        }
    }

    if (s1 + z1 === s2 + z2) {
        return s1 + z1;
    }

    if (s1 + z1 > s2 + z2 && z2 > 0) {
        return s1 + z1;
    }

    if (s2 + z2 > s1 + z1 && z1 > 0) {
        return s2 + z2;
    }

    return -1;

};

const test = () => {
    const params = [
        {
            input: { nums1: [0,16,28,12,10,15,25,24,6,0,0], nums2: [20,15,19,5,6,29,25,8,12] },
            output: 139,
        },
        {
            input: { nums1: [3,2,0,1,0], nums2: [6,5,0] },
            output: 12,
        },
        {
            input: { nums1: [2,0,2,0], nums2: [1,4] },
            output: -1,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums1, nums2 } = input;

        const result = minSum(nums1, nums2);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();