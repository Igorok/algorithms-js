function findLongestChain(pairs: number[][]): number {
    const arr: number[][] = [...pairs].sort((a: number[], b: number[]) => a[1] - b[1]);

    let res: number = 1;
    let prev: number[] = arr[0];
    for (let i: number = 1; i < arr.length; ++i) {
        if (arr[i][0] > prev[1]) {
            res += 1;
            prev = arr[i];
        }
    }

    return res;
};

/*

[1,2],[7,8],[4,5]
0 1 2 3 4 5 6 7 8 9 10
0 1-1 0 1-1 0 1-1 0 0

---

[1,2],[2,3],[3,4]
0 1 2 3 4 5
0 1-1
0 0 1-1
0 0 0 1-1

0 0 0 0 0 0 0 0 0
1 2
  1 2
    1 2
      1 2
        1 2
*/

const test = () => {
    const params = [
        {
            input: [[1,2],[2,3],[3,4]],
            output: 2,
        },
        {
            input: [[1,2],[7,8],[4,5]],
            output: 3,
        },
    ];

    params.forEach(({input, output}) => {
        const nums: number[][] = input;
        const result = findLongestChain(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();