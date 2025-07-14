function maxEvents_0(events: number[][]): number {
    events.sort((a, b) => a[1] - b[1]);

    let count: number = 0;
    let now: number = 1;

    for (let i: number = 0; i < events.length; ++i) {
        const [s, e] = events[i];
        if (now > e) {
            continue;
        }
        count += 1;
        if (now >= s && now <= e) {
            now += 1;
            continue;
        }
        if (now < s) {
            now = s+1;
        }
    }

    return count;
};

function maxEvents(events: number[][]): number {
    const data: number[][] = events.map(([s, e], id) => [s, e, id]);
    const visited: number[] = new Array(data.length).fill(0);

    const byStart: number[][] = [...data].sort((a, b) => {
        if (a[0] === b[0]) return a[1] - b[1];
        return a[0] - b[0];
    });

    const byEnd: number[][] = [...data].sort((a, b) => {
        if (a[1] === b[1]) return a[0] - b[0];
        return a[1] - b[1];
    });

    let i: number = 0;
    let j: number= 0;

    let now: number = 0;
    let count: number = 0;

    while (i < byStart.length || j < byEnd.length) {
        while (i < byStart.length && (visited[byStart[i][2]] || byStart[i][1] < now)) {
            i += 1;
        }
        while (j < byEnd.length && (visited[byEnd[j][2]] || byEnd[j][1] < now)) {
            j += 1;
        }

        if (j < byEnd.length && now < byEnd[j][0] && i < byStart.length && now >= byStart[i][0]) {
            visited[byStart[i][2]] = 1;
            now += 1;
            i += 1;
            count += 1;
            continue;
        }

        if (j < byEnd.length && now >= byEnd[j][0]) {
            visited[byEnd[j][2]] = 1;
            now += 1;
            j += 1;
            count += 1;
            continue;
        }

        now += 1;

    }

    return count;
};

/*

1 2 3 4 5 6
1 1 -1 -1
1 1 -1 -1
1      -1

*/

const test = () => {
    const params = [
        {
            input: {
                events: [[1,5],[1,5],[1,5],[2,3],[2,3]],
            },
            output: 5,
        },
        {
            input: {
                events: [[1,2],[2,3],[3,4]],
            },
            output: 3,
        },
        {
            input: {
                events: [[1,2],[2,3],[3,4],[1,2]]
            },
            output: 4,
        },
    ];

    params.forEach(({input, output}) => {
        const { events } = input;
        const result = maxEvents(events);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();