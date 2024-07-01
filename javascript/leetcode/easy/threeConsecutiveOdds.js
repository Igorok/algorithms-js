/*

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.

*/



/**
 * @param {number[]} arr
 * @return {boolean}
 */
var threeConsecutiveOdds = function(arr) {
    for (let i = 2; i < arr.length; ++i) {
        if (! Boolean(arr[i] % 2)) {
            continue;
        }

        let count = 1;
        for (let j = 1; j < 3; ++j) {
            if (
                Boolean(arr[i - j] % 2)
                && arr[i - j] <= arr[i - j + 1]
            ) {
                count += 1;

                if (count === 3) {
                    return true;
                }
            } else {
                break;
            }
        }
    }

    return false;
};

const test = () => {
    const params = [
        {
            input: [2,6,4,1],
            output: false,
        },
        {
            input: [1,2,34,3,4,5,7,23,12],
            output: true,
        },
        {
            input: [1,1,2,1,1],
            output: false,
        }
    ];

    params.forEach(({ input, output }) => {
        const result = threeConsecutiveOdds(input);
        console.log(
            result === output ? 'SUCCESS' : 'ERROR',
            'input', input,
            'output', output,
            'result', result,
        );
    });
}

test();
