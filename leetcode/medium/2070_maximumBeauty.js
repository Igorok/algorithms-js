/**
 * @param {number[][]} items
 * @param {number[]} queries
 * @return {number[]}
 */
var maximumBeauty = function(items, queries) {
    const arr = items.sort((a, b) => {
        if (b[1] === a[1]) return a[0] - b[0];
        return b[1] - a[1]
    });

    const res = queries.map((q) => {
        for (let i = 0; i < arr.length; ++i) {
            if (arr[i][0] <= q) {
                return arr[i][1];
            }
        }
        return 0;
    });


    console.log('arr', arr);



    return res;
};


const test = () => {
    const params = [
        {
            input: [[[1,2],[3,2],[2,4],[5,6],[3,5]], [1,2,3,4,5,6]],
            output: [2,4,5,5,6,6],
        },
        {
            input: [[[1,2],[1,2],[1,3],[1,4]], [1]],
            output: [4],
        },
        {
            input: [[[10,1000]], [5]],
            output: [0],
        },
    ];

    for (const { input, output } of params) {
        const [items, queries] = input;

        const result = maximumBeauty(items, queries);
        const message = `
            INPUT: ${input}
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


`
867954037 * 2 + 178424817


1735908074 + 178424817

1914332891


`
