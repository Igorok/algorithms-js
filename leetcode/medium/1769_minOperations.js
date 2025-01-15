/**
 * @param {string} boxes
 * @return {number[]}
 */
var minOperations_0 = function(boxes) {
    const left = new Array(boxes.length).fill(0);
    const right = new Array(boxes.length).fill(0);
    const res = new Array(boxes.length).fill(0);

    let balls = Number(boxes[0]);
    for (let i = 1; i < boxes.length; ++i) {
        left[i] = balls + left[i - 1];
        balls += Number(boxes[i]);
    }

    balls = Number(boxes.at(-1));
    for (let i = boxes.length - 2; i > -1; --i) {
        right[i] = balls + right[i + 1];
        balls += Number(boxes[i]);
    }


    for (let i = 0; i < boxes.length; ++i) {
        res[i] = left[i] + right[i]
    }

    return res;
};


var minOperations = function(boxes) {
    const left = new Array(boxes.length).fill(0);
    const right = new Array(boxes.length).fill(0);
    const res = new Array(boxes.length).fill(0);

    let balls = Number(boxes[0]);
    for (let i = 1; i < boxes.length; ++i) {
        left[i] = balls + left[i - 1];
        balls += Number(boxes[i]);
    }

    res[res.length - 1] = left.at(-1);

    balls = Number(boxes.at(-1));
    for (let i = boxes.length - 2; i > -1; --i) {
        right[i] = balls + right[i + 1];
        balls += Number(boxes[i]);

        res[i] = left[i] + right[i];
    }

    return res;
};




/*

1 1 0
0 1 2

*/



const test = () => {
    const params = [
        {
            input: '110',
            output: [1,1,3],
        },
        {
            input: '001011',
            output: [11,8,5,4,3,4],
        },
    ];

    params.forEach(({input, output}) => {
        const result = minOperations(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();