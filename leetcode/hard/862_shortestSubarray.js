/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var shortestSubarray_1 = function(nums, k) {
    let start = 0;
    let end = 0;

    let sum = nums[0];
    let res = nums.length + 1;
    while (end !== nums.length) {

        while (sum >= k) {
            if (end - start === 0) {
                return 1;
            }

            res = Math.min(res, (end - start + 1));
            sum -= nums[start];
            start += 1;
        }

        end += 1;
        if (end < nums.length) {
            sum += nums[end];
        }
    }

    return res === nums.length + 1 ? -1 : res;
};


var shortestSubarray_2 = function(nums, k) {
    class Deque {
        constructor (length) {
            this.start = 0;
            this.end = 0;
            this.arr = new Array(length + 1).fill(0);
        }
        length () {
            return (this.end - this.start) > 0;
        }
        first () {
            if (this.length()) {
                return this.arr[this.start];
            }
        }
        last () {
            if (this.length()) {
                return this.arr[this.end - 1];
            }
        }
        push (val) {
            this.arr[this.end] = val;
            this.end += 1;
        }
        pop () {
            if (this.length()) {
                const val = this.arr[this.end - 1];
                this.end -= 1;
                return val;
            }
        }
        popleft () {
            if (this.length()) {
                const val = this.arr[this.start];
                this.start += 1;
                return val;
            }
        }
    }

    const deque = new Deque(nums.length);
    let res = nums.length + 1;
    let sum = 0;

    for (let i = 0; i < nums.length; ++i) {
        sum += nums[i];

        if (sum >= k) {
            res = Math.min(res, i + 1);
        }

        while (deque.length() && sum - deque.first()[1] >= k) {
            const [fI, fS] = deque.popleft();
            res = Math.min(res, i - fI);
        }

        while (deque.length() && deque.last()[1] >= sum) {
            deque.pop();
        }

        deque.push([i, sum]);
    }

    return res === nums.length + 1 ? -1 : res;
};


var shortestSubarray = function(nums, k) {
    const deque = [];
    let res = nums.length + 1;
    let sum = 0;

    for (let i = 0; i < nums.length; ++i) {
        sum += nums[i];

        if (sum >= k) {
            res = Math.min(res, i + 1);
        }

        while (deque.length && sum - deque[0][1] >= k) {
            const [fI, fS] = deque.shift();
            res = Math.min(res, i - fI);
        }

        while (deque.length && deque[deque.length - 1][1] >= sum) {
            deque.pop();
        }

        deque.push([i, sum]);
    }

    return res === nums.length + 1 ? -1 : res;
};

/*

[1,2,3,4,-8, 14], 10

1 3 6 10 2 16

1 3 6 10
= 4

1 3 6 10 2

1 2

1 2 16
= 3

2 16
= 2

16
=1



*/


const test = () => {
    const params = [
        // {
        //     input: [[1], 1],
        //     output: 1,
        // },

        // {
        //     input: [[1,2], 4],
        //     output: -1,
        // },
        // {
        //     input: [[2,-1,2], 3],
        //     output: 3,
        // },
        // {
        //     input: [[84,-37,32,40,95], 167],
        //     output: 3,
        // },
        {
            input: [[1, 2, 3, 4, -8, 14], 10],
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const result = shortestSubarray(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();