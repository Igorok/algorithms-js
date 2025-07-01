function sortItems(
    n: number,
    m: number,
    group: number[],
    beforeItems: number[][],
): number[] {
    return [];
}

/*

n: 8, m: 2,
group: [
0:  -1,
1:  -1,
2:  1,
3:  0,
4:  0,
5:  1,
6:  0,
7:  -1
],
beforeItems: [
0:  [],
1:  [6],
2:  [5],
3:  [6],
4:  [3, 6],
5:  [],
6:  [],
7:  []
],

-1: 0, 1, 7
 0: 3, 4, 6,
 1: 2, 5,

0, 7, 5, 2, 6, 3, 4, 1

---

n: 8, m: 2,
group: [
0:  -1,
1:  -1,
2:  1,
3:  0,
4:  0,
5:  1,
6:  0,
7:  -1
],
beforeItems: [
0:  [],
1:  [6],
2:  [5],
3:  [6],
4:  [3],
5:  [],
6:  [4],
7:  []
],

-1: 0, 1, 7
 0: 3, 4, 6
 1: 2, 5

0, 7, 5, 2, ...

*/

const test = () => {
    const params = [
        {
            input: {
                n: 8,
                m: 2,
                group: [-1, -1, 1, 0, 0, 1, 0, -1],
                beforeItems: [[], [6], [5], [6], [3, 6], [], [], []],
            },
            output: [6, 3, 4, 1, 5, 2, 0, 7],
        },
        {
            input: {
                n: 8,
                m: 2,
                group: [-1, -1, 1, 0, 0, 1, 0, -1],
                beforeItems: [[], [6], [5], [6], [3], [], [4], []],
            },
            output: [],
        },
    ];

    params.forEach(({ input, output }) => {
        const { n, m, group, beforeItems } = input;
        const result = sortItems(n, m, group, beforeItems);

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
