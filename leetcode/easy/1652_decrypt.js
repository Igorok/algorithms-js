/**
 * @param {number[]} code
 * @param {number} k
 * @return {number[]}
 */
var decrypt_1 = function(code, k) {
    if (k === 0) return new Array(code.length).fill(0);

    const forward = k > 0;
    const steps = Math.abs(k);
    const res = [];
    // let sum = 0;

    const getId = (i, step) => {
        if (forward) {
            return (i + step) % code.length;
        }
        let id = i - step;
        if (id < 0) {
            id += code.length;
        }
        return id;
    };




    for (let i = 0; i < code.length; ++i) {
        let sum = 0;
        for (let j = 1; j <= steps; ++j) {
            const id = getId(i, j);
            sum += code[id];
        }
        res.push(sum);
    }


    return res;
};


var decrypt = function(code, k) {
    const res = new Array(code.length).fill(0);
    if (k === 0) return res;

    const forward = k > 0;
    const steps = Math.abs(k);

    const getId = (i, step) => {
        if (forward) {
            return (i + step) % code.length;
        }
        let id = i - step;
        if (id < 0) {
            id += code.length;
        }
        return id;
    };

    // start
    let sum = 0;
    for (let j = 1; j <= steps; ++j) {
        const id = getId(0, j);
        sum += code[id];
    }
    res[0] = sum;

    for (let i = 1; i < code.length; ++i) {
        const prevId = forward ? getId(i - 1, 1) : getId(i - 1, steps);
        sum -= code[prevId];

        const nextId = forward ? getId(i, steps) : getId(i, 1);
        sum += code[nextId];

        res[i] = sum;
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: [[5,7,1,4], 3],
            output: [12,10,16,13],
        },
        {
            input: [[1,2,3,4], 0],
            output: [0,0,0,0],
        },
        {
            input: [[2,4,9,3], -2],
            output: [12,5,6,13],
        },
    ];

    for (const { input, output } of params) {
        const result = decrypt(...input);
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
