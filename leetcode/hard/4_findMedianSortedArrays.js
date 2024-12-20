/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays_1 = function(nums1, nums2) {
    let i = j = 0;
    const merged = [];
    while (i < nums1.length && j < nums2.length) {
        if (nums1[i] < nums2[j]) {
            merged.push(nums1[i]);
            ++i;
        } else {
            merged.push(nums2[j]);
            ++j;
        }
    }

    while (i < nums1.length) {
        merged.push(nums1[i]);
        ++i;
    }

    while (j < nums2.length) {
        merged.push(nums2[j]);
        ++j;
    }

    if ((merged.length % 2) === 1) {
        return merged[Math.floor(merged.length / 2)];
    }

    const rId = Math.floor(merged.length / 2);

    return (merged[rId-1] + merged[rId]) / 2;
};

/*

1 2 3 4 5 6 7 8 9
        5 6 7 8 9 10 11 12

1 2 3 4 5 5 6 6 7 7 8 8 9 9 10 11 12
l 17, m 8, v 7

l1 9,
l2 8,

---

1 1 1
1 1 1

---

1 2 3
4 5 6

1 2 3
        4 5 6
n + m
median = (m + n) / 2; 6 / 2 = 3; (i2+i3)/2 = 3.5;

i3 - ?

---

1 2 3
3 4 5 6 7

1 2 3
    3 4 5 6 7
n + m
median = (m + n) / 2; 8 / 2 = 4; (i3+i4)/2 = 3.5;

i3 - ?
i4 - ?

---

1 2 3 4 5
6 7

---

1 2
3 4 5 6 7 8

*/
var findMedianSortedArrays = function(nums1, nums2) {
    const length = nums1.length + nums2.length;
    const median = Math.floor(length / 2);
    const isOdd = Boolean(length % 2);

    let small = nums1;
    let big = nums2;
    if (nums1.length > nums2.length) {
        small = nums2;
        big = nums1;
    }

    let i = 0;
    let j = small.length - 1;

    while (true) {
        const smallId = Math.floor((i + j) / 2);
        // two 0 indexed arrays
        const bigId = median - smallId - 2;

        const smallLeft = smallId >= 0 ? small[smallId] : Number.MIN_SAFE_INTEGER;
        const smallRight = smallId + 1 < small.length ? small[smallId + 1] : Number.MAX_SAFE_INTEGER;
        const bigLeft = bigId >= 0 ? big[bigId] : Number.MIN_SAFE_INTEGER;
        const bigRight = bigId + 1 < big.length ? big[bigId + 1] : Number.MAX_SAFE_INTEGER;

        if (smallLeft <= bigRight && bigLeft <= smallRight) {
            if (isOdd) {
                return Math.min(smallRight, bigRight);
            } else {
                return (Math.max(smallLeft, bigLeft) + Math.min(smallRight, bigRight)) / 2;
            }
        } else if (smallLeft > bigRight) {
            j = smallId - 1;
        } else {
            i = smallId + 1;
        }
    }

    return 0;
};

const test = () => {
    const getArray = () => {
        const limitLength = 100_000;
        const limitNum = 1_000_000;
        const length = Math.floor(Math.random() * limitLength);
        const arr = [];
        for (let i = 0; i < length; ++i) {
            arr.push(Math.floor(Math.random() * limitNum));
        }
        return arr.sort((a, b) => a - b);
    };


    const params = [
        { input: [[1, 3], [2]] },
        { input: [[1, 2], [3, 4]] },
        { input: [[1, 2, 3], [3, 4, 5, 6, 7]] },
        { input: [[1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9, 10, 11, 12]] },
    ];
    for (let i = 0; i < 10; ++i) {
        params.push({ input: [getArray(), getArray()] });
    }

    params.forEach(({input}) => {
        const output = findMedianSortedArrays_1(...input);
        const result = findMedianSortedArrays(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            // 'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};




/*
const test = () => {
    const params = [
        {
            input: [[1,3], [2]],
            output: 2,
        },
        {
            input: [[1,2], [3,4]],
            output: 2.5,
        },
    ];

    params.forEach(({input, output}) => {
        const result = findMedianSortedArrays(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};
*/

test();
