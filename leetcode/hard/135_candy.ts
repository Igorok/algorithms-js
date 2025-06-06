function candy(ratings: number[]): number {
    const children: number[][] = ratings.map((r, i) => [r, i]).sort((a, b) => a[0] - b[0]);

    const count: number[] = new Array(ratings.length).fill(0);
    let res: number = 0;


    for (const [rating, id] of children) {
        count[id] = 1;
        if (id < ratings.length-1 && rating > ratings[id+1]) {
            count[id] = Math.max(count[id], count[id+1] + 1);
        }

        if (id > 0 && rating > ratings[id-1]) {
            count[id] = Math.max(count[id], count[id-1] + 1);
        }

        res += count[id];
    }


    return res;
};


/*

0 1 2
1 2 3

*/

const test = () => {
    const params = [
        {
            input: {
                ratings: [1,0,2]
            },
            output: 5,
        },
        {
            input: {
                ratings: [1,2,2]
            },
            output: 4,
        },
    ];

    params.forEach(({input, output}) => {
        const { ratings } = input;
        const result = candy(ratings);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();