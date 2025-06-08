function canReach(arr: number[], start: number): boolean {
    let zerosCount: number = 0;

    const visited: number[] = new Array(arr.length).fill(0);

    const dfs = (id: number) => {
        if (visited[id] === 1) {
            return;
        }

        visited[id] = 1;

        if (arr[id] === 0) {
            zerosCount += 1;
        }

        if (id - arr[id] > -1) {
            dfs(id - arr[id]);
        }
        if (id + arr[id] < arr.length) {
            dfs(id + arr[id]);
        }
    };

    dfs(start);


    return zerosCount !== 0;
};

/*

6
0 1 2 3 4 5 6
0,3,0,6,3,3,4


*/

const test = () => {
    const params = [
        {
            input: { arr: [0,3,0,6,3,3,4], start: 6 },
            output: true,
        },
        {
            input: { arr: [4,2,3,0,3,1,2], start: 5 },
            output: true,
        },
        {
            input: { arr: [4,2,3,0,3,1,2], start: 0 },
            output: true,
        },
        {
            input: { arr: [3,0,2,1,2], start: 2 },
            output: false,
        },
    ];

    params.forEach(({input, output}) => {
        const { arr, start } = input;
        const result = canReach(arr, start);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();