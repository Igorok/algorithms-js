
function longestObstacleCourseAtEachPosition(obstacles: number[]): number[] {
    const sequence: number[] = [];

    const binSearch = (num: number): number => {
        let start: number = 0;
        let end: number = sequence.length - 1;
        let res: number = 0;

        while (start <= end) {
            const middle: number = Math.floor((start + end) / 2);

            if (sequence[middle] > num) {
                res = middle;
                end = middle - 1;
            } else {
                start = middle + 1;
            }
        }

        return res;
    };

    const res: number[] = [];

    for (const num of obstacles) {
        if (!sequence.length || sequence.at(-1) <= num) {
            sequence.push(num);
            res.push(sequence.length);
            continue;
        }

        const id: number = binSearch(num);
        sequence[id] = num;

        res.push(id + 1);
    }

    return res;
};


/*
[3,1,5,6,4,2]
[1,1,2,3,2,2]

3   3
1   3
5   1,5
6   1,5,6
4   1,4
2   1,2

1,2,6

1 2 1 2 1 2 1 2
1 2 2 3 3 4 4 5

1   1
2   1 2
1   1 1
2   1 1 2
1   1 1 1
2   1 1 1 2
1   1 1 1 1
2   1 1 1 1 2


*/

const test = () => {
    const params = [
        {
            input: { obstacles: [1,2,3,2] },
            output: [1,2,3,3],
        },
        {
            input: { obstacles: [2,2,1] },
            output: [1,2,1],
        },
        {
            input: { obstacles: [3,1,5,6,4,2] },
            output: [1,1,2,3,2,2],
        },
    ];

    params.forEach(({input, output}) => {
        const { obstacles } = input;

        const result = longestObstacleCourseAtEachPosition(obstacles);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();