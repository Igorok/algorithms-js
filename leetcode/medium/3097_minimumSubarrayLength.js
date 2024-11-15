/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minimumSubarrayLength = function(nums, k) {
    class BitManager {
        constructor (num) {
            this.memo = new Array(32).fill(0);
            this.addBit(num);
        }
        updateMemo(num, plus) {
            const arr = parseInt(num).toString(2).split('').reverse();
            for (let i = 0; i < arr.length; ++i) {
                if (arr[i] === '1') {
                    this.memo[i] += plus ? 1 : -1;
                }
            }
        }
        addBit(num) {
            this.updateMemo(num, true);
        }
        removeBit(num) {
            this.updateMemo(num);
        }
        getNum() {
            const memo = this.memo.map((n) => n == 0 ? 0 : 1).reverse().join('');
            return parseInt(memo, 2)
        }
    }

    let start = end = 0;
    const bitManager = new BitManager(nums[0]);

    let res = -1;
    while (end < nums.length) {
        if (bitManager.getNum() < k) {
            end += 1;
            bitManager.addBit(nums[end]);
        } else {
            if (res === -1) {
                res = end - start + 1;
            }
            res = Math.min(res, (end - start + 1));
            if (res === 1) {
                return 1;
            }
            bitManager.removeBit(nums[start]);
            start += 1;
        }
    }


    return res;
};



const test = () => {
    const params = [
        {
            input: [[1,2,3], 2],
            output: 1,
        },
        {
            input: [[2,1,8], 10],
            output: 3,
        },
        {
            input: [[1,2], 0],
            output: 1,
        },
        {
            input: [[3,1,4,2,5,8], 6],
            output: 1,
        },
    ];

    for (const { input, output } of params) {
        const result = minimumSubarrayLength(...input);
        const message = `
            INPUT: ${input}
            OUTPUT: ${output}
            RESULT: ${result}
            `;

        if (result === output) {
            console.log(
                'SUCCESS: \n', message,
            );
        } else {
            console.error('ERROR: \n', message);
        }
    }
};

test();
