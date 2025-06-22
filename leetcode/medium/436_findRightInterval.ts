function findRightInterval(intervals: number[][]): number[] {
    const ends: number[][] = intervals.map(([start, end], id) => [start, id]);
    ends.sort((a, b) => a[0] - b[0]);

    const getId = (num: number, id: number): number => {
        let left: number = 0;
        let right: number = ends.length - 1;

        let res: number = -1;
        while (left <= right) {
            const middle: number = Math.floor((left + right) / 2);

            if (ends[middle][0] >= num) {
                if (id !== ends[middle][1]) {
                    res = middle;
                } else if (middle < ends.length - 1) {
                    res = middle + 1;
                }

                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }

        return res === -1 ? res : ends[res][1];
    };

    return intervals.map(([start, end], id) => {
        if (start === end) return id;
        return getId(end, id);
    });
};


/*

[1, 2], [1, 2], [1, 2], [1, 2],
[]


*/

const test = () => {
    const params = [
        {
            input: {
                intervals: [[1,1],[3,4]]
            },
            output: [0,-1],
        },
        {
            input: {
                intervals: [[1,4],[2,3],[3,4]]
            },
            output: [-1,2,-1],
        },
        {
            input: {
                intervals: [[3,4],[2,3],[1,2]]
            },
            output: [-1,0,1],
        },
        {
            input: {
                intervals: [[1,2]]
            },
            output: [-1],
        },
    ];

    params.forEach(({input, output}) => {
        const { intervals } = input;
        const result = findRightInterval(intervals);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

