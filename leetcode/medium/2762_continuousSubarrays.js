/**
 * @param {number[]} nums
 * @return {number}
 */
var continuousSubarrays_1 = function(nums) {
    let res = 0;
    for (let i = 0; i < nums.length; ++i) {
        let min = nums[i];
        let max = nums[i];
        let count = 1;
        for (let j = i + 1; j < nums.length; ++j) {
            min = Math.min(min, nums[j]);
            max = Math.max(max, nums[j]);
            if (max - min > 2) {
                break;
            }
            count += 1;
        }
        res += count;
    }

    return res;
};

/*

1 2 3 4 5

1 2 3
      4 5
? 3 4

5 4 2 4
5 4         3
  4 2 4     1+2+3



31 30 31 32     4 + 2

1 2 2 3 2 2 2 4

4 2 2 3 2 2 2 1 2 2 2 2






4 2 4 3 4 3 2 1 2 2 2 2




*/

var continuousSubarrays = function(nums) {
    let res = 0;
    const count = {};
    let left = right = 0;

    while (right < nums.length) {
        // we can meet a max or min twice
        count[nums[right]] = (count[nums[right]] || 0) + 1;

        // if condition max - min < 2 is broken
        // we will traverse to right
        while (Math.max(...Object.keys(count)) - Math.min(...Object.keys(count)) > 2) {
            count[nums[left]] -= 1;
            if (count[nums[left]] === 0) {
                delete count[nums[left]];
            }
            left += 1;
        }

        // every new number give us a new array for every length
        // 0+1=1 - 1 array with length 1
        // 1+1=2 - 1 array with length 1 and 1 array with length 2
        // 2+1=3 - 1 array with length 1, 1 array with length 2 and 1 array with length 3
        const length = right - left + 1;
        res += length;

        right += 1;
    }

    return res;
};



const test = () => {
    const params = [
        {
            input: [5,4,2,4],
            output: 8,
        },
        {
            input: [1,2,3],
            output: 6,
        },
        {
            input: [31,30,31,32],
            output: 10,
        },

        {
            input: [65,66,67,66,66,65,64,65,65,64],
            output: 43,
        },


    ];

    params.forEach(({input, output}) => {
        const result = continuousSubarrays(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();