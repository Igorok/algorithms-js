/**
 * @param {number[]} nums
 * @param {number} limit
 * @return {number[]}
 */
var lexicographicallySmallestArray_0 = function(nums, limit) {
    const arr = [...nums];
    const replace = (i) => {
        let smallId = i;
        for (let j = i + 1; j < arr.length; ++j) {
            if (arr[i] > arr[j] && (arr[i] - arr[j]) <= limit && arr[j] < arr[smallId]) {
                smallId = j;
            }
        }
        if (smallId !== i) {
            const tmp = arr[i];
            arr[i] = arr[smallId];
            arr[smallId] = tmp;
            replace(i);
        }
    };
    for (let i = 0; i < arr.length - 1; ++i) {
        replace(i);
    }

    return arr;
};

var lexicographicallySmallestArray = function(nums, limit) {
    const arr = [...nums];
    const replace = (i) => {
        let smallId = i;
        for (let j = i + 1; j < arr.length; ++j) {
            if (arr[i] > arr[j] && (arr[i] - arr[j]) <= limit && arr[j] < arr[smallId]) {
                smallId = j;
            }
        }
        if (smallId !== i) {
            const tmp = arr[i];
            arr[i] = arr[smallId];
            arr[smallId] = tmp;
            replace(i);
        }
    };
    for (let i = 0; i < arr.length - 1; ++i) {
        replace(i);
    }

    return arr;
};


/*

[4,52,38,59,71,27,31,83,88,10], 14




*/

const test = () => {
    const params = [
        {
            input: [[1,5,3,9,8], 2],
            output: [1,3,5,8,9],
        },
        {
            input: [[1,7,6,18,2,1], 3],
            output: [1,6,7,18,1,2],
        },
        {
            input: [[1,7,28,19,10], 3],
            output: [1,7,28,19,10],
        },
        {
            input: [[1,60,34,84,62,56,39,76,49,38], 4],
            output: [1,56,34,84,60,62,38,76,49,39],
        },
        {
            input: [[4,52,38,59,71,27,31,83,88,10], 14],
            output: [4,27,31,38,52,59,71,83,88,10],
        },
    ];

    for (const { input, output } of params) {
        const result = lexicographicallySmallestArray(...input);
        const message = `
            INPUT: ${JSON.stringify(input)}
            OUTPUT: ${output}
            RESULT: ${result}
            `;

        if (JSON.stringify(result) === JSON.stringify(output)) {
            console.log(
                'SUCCESS: \n', message,
            );
        } else {
            console.error('ERROR: \n', message);
        }
    }
};

test();
