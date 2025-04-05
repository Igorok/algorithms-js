function subsetXORSum_0(nums: number[]): number {
    const getXor = (arr: number[]): number => {
        let res: number = 0;
        for (const num of arr) {
            res ^= num;
        }
        return res;
    };

    let res = 0;
    const rec = (id: number, acc: number[]): void => {
        if (id >= nums.length) {
            res += getXor(acc);
            return;
        }

        acc.push(nums[id]);
        rec(id+1, acc);

        acc.pop();
        rec(id+1, acc);
    };

    rec(0, []);

    return res;
};

function subsetXORSum(nums: number[]): number {
    let allBits: number = 0;

    for (const num of nums) {
        allBits |= num;
    }

    return allBits * 2**(nums.length-1);
};


/*

2 2

0 0
2 2
2 0
0 2

00 00 = 00
10 10 = 00
10 00 = 10
00 10 = 10

---

5 - 101
1 - 001
6 - 110

---

3 0011
4 0100
5 0101
6 0110
7 0111
8 1000

111100000

*/


const test = () => {
    const params = [
        {
            input: [1,3],
            output: 6,
        },
        {
            input: [5,1,6],
            output: 28,
        },
        {
            input: [3,4,5,6,7,8],
            output: 480,
        },
    ];

    params.forEach(({input, output}) => {
        const result = subsetXORSum(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();