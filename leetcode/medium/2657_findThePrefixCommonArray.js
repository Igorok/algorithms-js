/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number[]}
 */
var findThePrefixCommonArray = function(A, B) {
    const allNumbers = new Map();
    let count = 0;
    const res = new Array(A.length).fill(0);

    for (let i = 0; i < A.length; ++i) {
        const a = (allNumbers.get(A[i]) || 0) + 1;
        allNumbers.set(A[i], a);
        if (a === 2) {
            count += 1;
        }

        const b = (allNumbers.get(B[i]) || 0) + 1;
        allNumbers.set(B[i], b);
        if (b === 2) {
            count += 1;
        }

        res[i] = count;
    }

    return res;
};


const test = () => {
    const params = [
        {
            input: [[1,3,2,4], [3,1,2,4]],
            output: [0,2,3,4],
        },
        {
            input: [[2,3,1], [3,1,2]],
            output: [0,1,3],
        },
    ];

    params.forEach(({input, output}) => {
        const result = findThePrefixCommonArray(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();