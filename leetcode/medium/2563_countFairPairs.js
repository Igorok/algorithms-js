/**
 * @param {number[]} nums
 * @param {number} lower
 * @param {number} upper
 * @return {number}
 */
var countFairPairs = function(nums, lower, upper) {
    const arr = nums.sort((a, b) => a - b);

    console.log(
        'arr', arr,
        'lower', lower,
        'upper', upper,
    );

    const findRight = (s, val) => {
        let start = s;
        let end = arr.length - 1;

        let id = -1;
        while (start <= end) {
            const middle = Math.floor((start + end) / 2);
            if (arr[middle] > val) {
                end = middle - 1;
            } else if (arr[middle] <= val) {
                id = middle;
                start = middle + 1;
            }
        }
        return id;
    };

    const findLeft = (s, val) => {
        let start = s;
        let end = arr.length - 1;

        let id = -1;
        while (start <= end) {
            const middle = Math.floor((start + end) / 2);
            if (arr[middle] >= val) {
                id = middle;
                end = middle - 1;
            } else if (arr[middle] < val) {
                start = middle + 1;
            }
        }
        return id;
    };


    let res = 0;

    for (let i = 0; i < arr.length - 1; ++i) {
        if (arr[i] > 0 && (arr[i] > upper || arr[i] + arr[i+1] > upper)) {
            break;
        }

        const num = arr[i];
        const left = Math.max(lower - num, num);
        const right = upper - num;

        const lId = findLeft(i+1, left);
        const rId = findRight(i+1, right);

        if (lId === -1 || rId === -1) continue;



        console.log(
            'num', num,
            'left', left,
            'right', right,
            'lId', lId,
            'rId', rId,
            'rId - lId', rId - lId,
        );

        if (rId >= lId) {
            res += (rId - lId + 1);
        }
    }



    return res;

};


/*

[ 0, 1, 4, 4, 5, 7 ]
3 6
6
[ 1, 2, 5, 7, 9 ]
11 11
1
*/


const test = () => {
    const params = [
        // {
        //     input: [[0,1,7,4,4,5], 3, 6],
        //     output: 6,
        // },
        // {
        //     input: [[1,7,9,2,5], 11, 11],
        //     output: 1,
        // },
        // {
        //     input: [[2,2,2,2], 4, 4],
        //     output: 6,
        // },
        // {
        //     input: [[6,9,4,2,7,5,10,3], 13, 13],
        //     output: 3,
        // },
        {
            input: [[-5,-7,-5,-7,-5], -12, -12],
            output: 6,
        },



    ];

    for (const { input, output } of params) {
        const result = countFairPairs(...input);
        const message = `
            INPUT: ${JSON.stringify(input)}
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
