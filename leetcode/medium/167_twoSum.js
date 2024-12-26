/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    const findNumber = (_start, val) => {
        let start = _start;
        let end = numbers.length-1;

        if (val < numbers[start] || val > numbers[end]) return -1;

        while (start <= end) {
            const m = Math.floor((start + end) / 2);
            if (numbers[m] === val) {
                return m;
            } else if (numbers[m] > val) {
                end = m - 1;
            } else {
                start = m + 1;
            }
        }

        return -1;
    };

    for (let i = 0; i < numbers.length - 1; ++i) {
        const n = numbers[i];
        const v = target - n;
        const id = findNumber(i+1, v);
        if (id !== -1) {
            return [i+1, id+1];
        }
    }

    return [];
};


const test = () => {
    const params = [
        {
            input: [[2,7,11,15], 9],
            output: [1,2],
        },
        {
            input: [[2,3,4], 6],
            output: [1,3],
        },
        {
            input: [[-1,0], -1],
            output: [1,2],
        },
    ];

    params.forEach(({input, output}) => {
        const result = twoSum(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();