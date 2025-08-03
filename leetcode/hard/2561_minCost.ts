function minCost_0(basket1: number[], basket2: number[]): number {
    basket1.sort((a, b) => a - b);
    basket2.sort((a, b) => a - b);

    console.log(
        JSON.stringify(basket1), JSON.stringify(basket2)
    );





    const bothBasketNumbers: Map<number, number[]> = new Map();
    const pushNumber = (num: number, bId: number) => {
        const arr: number[] = bothBasketNumbers.get(num) || [0, 0];
        arr[bId] += 1;
        bothBasketNumbers.set(num, arr);
    };
    for (let i: number = 0; i < basket1.length; ++i) {
        pushNumber(basket1[i], 0);
        pushNumber(basket2[i], 1);
    }

    const nums1: number[][] = [];
    const nums2: number[][] = [];
    let forExchange = 0;

    for (const key of bothBasketNumbers.keys()) {
        const [cnt1, cnt2] = bothBasketNumbers.get(key);
        if ((cnt1 + cnt2) % 2) {
            return -1;
        }

        if (cnt1 === cnt2) {
            continue;
        }

        const middle: number = (cnt1 + cnt2) / 2;
        if (cnt1 > middle) {
            forExchange += cnt1 - middle;
            nums1.push([key, cnt1 - middle]);
        } else {
            nums2.push([key, cnt2 - middle]);
        }
    }

    nums1.sort((a, b) => a[0]-b[0]);
    nums2.sort((a, b) => a[0]-b[0]);

    let cnt: number = 0;
    let i1: number = 0;
    let i2: number = 0;
    let res: number = 0;
    while (cnt < forExchange) {
        if (nums1[i1][0] <= nums2[i2][0]) {
            cnt += nums1[i1][1];
            res += nums1[i1][1] * nums1[i1][0];
            i1 += 1;
        } else {
            cnt += nums2[i2][1];
            res += nums2[i2][1] * nums2[i2][0];
            i2 += 1;
        }
    }

    return res;
};

function minCost_1(basket1: number[], basket2: number[]): number {
    const bothBasketNumbers: Map<number, number[]> = new Map();
    const pushNumber = (num: number, bId: number) => {
        const arr: number[] = bothBasketNumbers.get(num) || [0, 0];
        arr[bId] += 1;
        bothBasketNumbers.set(num, arr);
    };
    for (let i: number = 0; i < basket1.length; ++i) {
        pushNumber(basket1[i], 0);
        pushNumber(basket2[i], 1);
    }

    const nums1: number[][] = [];
    const nums2: number[][] = [];
    const equal: number[][] = [];
    let forExchange = 0;

    for (const key of bothBasketNumbers.keys()) {
        const [cnt1, cnt2] = bothBasketNumbers.get(key);
        if ((cnt1 + cnt2) % 2) {
            return -1;
        }

        if (cnt1 === cnt2) {
            equal.push([key, cnt1 * 2]);
            continue;
        }

        const middle: number = (cnt1 + cnt2) / 2;
        if (cnt1 > middle) {
            forExchange += cnt1 - middle;
            nums1.push([key, cnt1 - middle]);
        } else {
            nums2.push([key, cnt2 - middle]);
        }
    }

    nums1.sort((a, b) => a[0]-b[0]);
    nums2.sort((a, b) => a[0]-b[0]);
    equal.sort((a, b) => a[0]-b[0]);

    let cnt: number = 0;
    let i1: number = 0;
    let i2: number = 0;
    let i3: number = 0;
    let res: number = 0;
    while (cnt < forExchange) {
        if (equal[i3][0] < nums1[i1][0] && equal[i3][0] < nums2[i2][0]) {
            let diff: number = forExchange - cnt;
            if (diff >= equal[i3][1]) {
                cnt += equal[i3][1];
                res += equal[i3][1] * equal[i3][0];
                i3 += 1;
                continue;
            }
            if (diff > 1) {
                diff = (diff & 1) ? diff - 1 : diff;
                cnt += diff;
                res += diff * equal[i3][0];
                equal[i3][1] -= diff;
                continue;
            }

        }

        if (nums1[i1][0] <= nums2[i2][0]) {
            cnt += nums1[i1][1];
            res += nums1[i1][1] * nums1[i1][0];
            i1 += 1;
        } else {
            cnt += nums2[i2][1];
            res += nums2[i2][1] * nums2[i2][0];
            i2 += 1;
        }
    }

    return res;
};

function minCost(basket1: number[], basket2: number[]): number {
    const bothBasketNumbers: Map<number, number[]> = new Map();
    const pushNumber = (num: number, bId: number) => {
        const arr: number[] = bothBasketNumbers.get(num) || [0, 0];
        arr[bId] += 1;
        bothBasketNumbers.set(num, arr);
    };
    for (let i: number = 0; i < basket1.length; ++i) {
        pushNumber(basket1[i], 0);
        pushNumber(basket2[i], 1);
    }

    const nums1: number[] = [];
    const nums2: number[] = [];
    let minEqual: number = Number.MAX_SAFE_INTEGER;

    for (const key of bothBasketNumbers.keys()) {
        const [cnt1, cnt2] = bothBasketNumbers.get(key);
        if ((cnt1 + cnt2) % 2) {
            return -1;
        }

        if (cnt1 === cnt2) {
            for (let i: number = 0; i < cnt1; ++i) {
                minEqual = Math.min(minEqual, key);
            }
            continue;
        }

        const middle: number = (cnt1 + cnt2) / 2;
        if (cnt1 > middle) {
            for (let i: number = 0; i < cnt1-middle; ++i) {
                nums1.push(key)
            }
        } else {
            for (let i: number = 0; i < cnt2-middle; ++i) {
                nums2.push(key)
            }
        }
    }

    nums1.sort((a, b) => a-b);
    nums2.sort((a, b) => a-b);

    console.log(
        JSON.stringify(nums1),
        JSON.stringify(nums2),
    );

    let cnt: number = 0;
    let i1: number = 0;
    let i2: number = 0;
    let res: number = 0;

    while (cnt < nums1.length) {
        if ((2 * minEqual) < Math.min(nums1[i1], nums2[i2])) {
            cnt += 1;
            res += 2 * minEqual;
            continue;
        }

        if (nums1[i1] <= nums2[i2]) {
            minEqual = Math.min(minEqual, nums1[i1]);
            cnt += 1;
            res += nums1[i1];
            i1 += 1;

            continue;
        }

        minEqual = Math.min(minEqual, nums2[i2]);
        cnt += 1;
        res += nums2[i2];
        i2 += 1;
    }


    return res;
};


/*

53
31,251,750,1104,1577,1749,2004,2492,2712,2820,2997,3350,3365,3847
205,644,925,1088,1098,1267,1920,1969,2317,2636,2882,3447,3772,3926

14
31 + 13*106


*/

const test = () => {
    const params = [
        {
            input: {
                basket1: [3350,1104,2004,1577,1365,2088,2249,1948,2621,750,31,2004,1749,3365,3350,3843,3365,1656,3168,3106,2820,3557,1095,2446,573,2464,2172,1326,2712,467,1104,1446,1577,53,2492,2638,1200,2997,3454,2492,1926,1452,2712,446,2997,2820,750,2529,3847,656,272,3873,530,1749,1743,251,3847,31,251,515,2858,126,2491],
                basket2: [530,1920,2529,2317,1969,2317,1095,2249,2858,2636,3772,53,3106,2638,1267,1926,2882,515,3772,1969,3454,2446,656,2621,1365,1743,3557,1656,3447,446,1098,1446,467,2636,1088,1098,2882,1088,1326,644,3873,3843,3926,1920,2464,2088,205,1200,1267,272,925,925,2172,2491,3168,644,1452,573,1948,3926,205,126,3447]
            },
            output: 837,
        },
        {
            input: {
                basket1: [84,80,43,8,80,88,43,14,100,88], basket2: [32,32,42,68,68,100,42,84,14,8]
            },
            output: 48,
        },
        {
            input: {
                basket1: [4,4,4,4,3], basket2: [5,5,5,5,3]
            },
            output: 8,
        },
        {
            input: {
                basket1: [4,2,2,2], basket2: [1,4,1,2]
            },
            output: 1,
        },
        {
            input: {
                basket1: [2,3,4,1], basket2: [3,2,5,1]
            },
            output: -1,
        },
    ];

    params.forEach(({input, output}) => {
        const { basket1, basket2 } = input;
        const result = minCost(basket1, basket2);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();