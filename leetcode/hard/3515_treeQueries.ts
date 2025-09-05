function treeQueries(n: number, edges: number[][], queries: number[][]): number[] {
    return [];
};

/*

 0
 1
2 4
6 5
3

*/


const test = () => {
    const params = [
        {
            input: {
                n: 2, edges: [[1,2,7]], queries: [[2,2],[1,1,2,4],[2,2]]
            },
            output: [7,4],
        },
        {
            input: {
                n: 3, edges: [[1,2,2],[1,3,4]], queries: [[2,1],[2,3],[1,1,3,7],[2,2],[2,3]]
            },
            output: [0,4,2,7],
        },
        {
            input: {
                n: 4, edges: [[1,2,2],[2,3,1],[3,4,5]], queries: [[2,4],[2,3],[1,2,3,3],[2,2],[2,3]]
            },
            output: [8,3,2,5],
        },
    ];

    params.forEach(({ input, output }) => {
        const { n, edges, queries } = input;
        const result = treeQueries(n, edges, queries);

        console.log(
            JSON.stringify(result) === JSON.stringify(output)
                ? "SUCCESS "
                : "ERROR ",
            "input",
            JSON.stringify(input),
            "output",
            output,
            "result",
            result,
        );
    });
};

test();
