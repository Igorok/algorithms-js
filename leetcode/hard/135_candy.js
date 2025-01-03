/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function(ratings) {
    const data = ratings.map((v, i) => ([v, i])).sort((a, b) => (a[0] - b[0]));
    const candies = new Array(ratings.length).fill(1);
    let res = 0;
    for (let i = 0; i < data.length; ++i) {
        const [raiting, id] = data[i];

        if (id - 1 !== -1 && raiting > ratings[id - 1]) {
            candies[id] = Math.max(candies[id], candies[id-1] + 1);
        };
        if (id + 1 !== data.length && raiting > ratings[id + 1]) {
            candies[id] = Math.max(candies[id], candies[id+1] + 1);
        };

        res += candies[id];
    }

    return res;

};

/*
3,2,1,0
4 3 2 1


29,51,87,87,72,12
1  2  3  3  2  1  = 12

*/

const test = () => {
    const params = [
        {
            input: [1,0,2],
            output: 5,
        },
        {
            input: [1,2,2],
            output: 4,
        },
        {
            input: [2,2,1],
            output: 4,
        },
        {
            input: [3,2,1,0],
            output: 10,
        },
        {
            input: [29,51,87,87,72,12],
            output: 12,
        },
    ];

    params.forEach(({input, output}) => {
        const result = candy(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();