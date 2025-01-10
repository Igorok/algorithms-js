/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    const filtered = citations.filter((v) => Boolean(v)).sort((a, b) => a - b);

    let res = 0;

    for (let i = 0; i < filtered.length; ++i) {
        const h = Math.min(
            filtered[i],
            filtered.length - i,
        );
        res = Math.max(res, h);
    }

    return res;

};


const test = () => {
    const params = [
        {
            input: [3,0,6,1,5],
            output: 3,
        },
        {
            input: [1,3,1],
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const result = hIndex(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();