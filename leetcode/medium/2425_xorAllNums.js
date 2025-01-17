/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var xorAllNums_0 = function(nums1, nums2) {
    const arr = [];
    for (const n1 of nums1) {
        for (const n2 of nums2) {
            arr.push(n1 ^ n2);
        }
    }

    return arr.reduce((acc, num) => (acc ^ num), 0);
};


var xorAllNums_1 = function(nums1, nums2) {
    let res = 0;
    for (const n1 of nums1) {
        let r = 0
        for (const n2 of nums2) {
            r ^= (n1 ^ n2);
        }
        res ^= r;
    }
    return res;
};

var xorAllNums_2 = function(nums1, nums2) {
    const one1 = [0];
    const one2 = [0];

    const rem1 = (nums1.length % 2);
    const rem2 = (nums2.length % 2);

    for (const num of nums1) {
        let n = num;
        let i = 0
        while (n !== 0) {
            if (!one1[i]) {
                one1[i] = 0;
            }
            const rem = n % 2;
            if (rem) {
                one1[i] += rem2;
                one1[i] %= 2;
            }
            n = Math.floor(n / 2);
            i += 1;
        }
    }

    for (const num of nums2) {
        let n = num;
        let i = 0
        while (n !== 0) {
            if (!one2[i]) {
                one2[i] = 0;
            }
            const rem = n % 2;
            if (rem) {
                one2[i] += rem1;
                one2[i] %= 2;
            }
            n = Math.floor(n / 2);
            i += 1;
        }
    }

    for (let i = 0; i < Math.max(one1.length, one2.length); ++i) {
        if (!one1[i]) one1[i] = 0;
        if (!one2[i]) one2[i] = 0;

        one1[i] = ((one1[i] + one2[i]) % 2);
    }

    return parseInt(one1.reverse().join(''), 2);
};

var xorAllNums = function(nums1, nums2) {
    const getXor = (arr, odd) => odd
        ? arr.reduce((acc, num) => (acc ^ num), 0)
        : 0;

    return getXor(nums1, nums2.length % 2) ^ getXor(nums2, nums1.length % 2);
};


const test = () => {
    const params = [
        {
            input: [[2,1,3], [10,2,5,0]],
            output: 13,
        },
        {
            input: [[1,2], [3,4]],
            output: 0,
        },
        {
            input: [[0], [0]],
            output: 0,
        },
    ];

    for (const { input, output } of params) {
        const result = xorAllNums(...input);
        const message = `
            INPUT: ${JSON.stringify(input)}
            OUTPUT: ${JSON.stringify(output)}
            RESULT: ${JSON.stringify(result)}`;

        if (JSON.stringify(result) === JSON.stringify(output)) {
            console.log(
                `SUCCESS: ${message}`,
            );
        } else {
            console.error(`ERROR: ${message}`);
        }
    }
};

test();
