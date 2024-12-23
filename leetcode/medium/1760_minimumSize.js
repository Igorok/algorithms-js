/**
 * @param {number[]} nums
 * @param {number} maxOperations
 * @return {number}
 */
var minimumSize_1 = function(nums, maxOperations) {
    const checkDivision = (num) => {
        let operations = 0;
        for (const n of nums) {
            const parts = Math.ceil(n / num);
            if (parts > 1) {
                // every division to 2 parts give us plus one bag, first bag we have initially
                operations += (parts - 1);
            }

            if (operations > maxOperations) return false;
        }

        return true;
    };

    const max = Math.max(...nums);
    let res = max;
    for (let i = max; i >= 0; --i) {
        if (checkDivision(i)) {
            res = i;
        }
    }

    return res;
};

var minimumSize = function(nums, maxOperations) {
    const checkDivision = (num) => {
        let operations = 0;
        for (const n of nums) {
            const parts = Math.ceil(n / num);
            if (parts > 1) {
                // every division to 2 parts give us plus one bag, first bag we have initially
                operations += (parts - 1);
            }

            if (operations > maxOperations) return false;
        }

        return true;
    };

    let start = 1;
    let end = Math.max(...nums);
    let res = end;

    while (start <= end) {
        const middle = Math.round((start + end) / 2);
        if (!checkDivision(middle)) {
            start = middle + 1;
        } else {
            res = middle;
            end = middle - 1;
        }
    }

    return res;
};

/*
9 3
3 - ? 3,6; 3,3;


*/



const test = () => {
    const params = [
        {
            input: [[9], 2],
            output: 3,
        },
        {
            input: [[2,4,8,2], 4],
            output: 2,
        },
        {
            input: [[431,922,158,60,192,14,788,146,788,775,772,792,68,143,376,375,877,516,595,82,56,704,160,403,713,504,67,332,26], 80],
            output: 129,
        }
    ];

    params.forEach(({input, output}) => {
        const result = minimumSize(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();