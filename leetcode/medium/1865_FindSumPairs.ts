class FindSumPairs_0 {
    nums1: number[];
    nums2: number[];
    countBySum: Map<number, number>;

    constructor(nums1: number[], nums2: number[]) {
        this.nums1 = nums1;
        this.nums2 = nums2;
        this.countBySum = new Map();

        for (const n2 of this.nums2 ) {
            for (const n1 of this.nums1) {
                const s: number = n2 + n1;

                const cnt: number = this.countBySum.get(s) || 0;
                this.countBySum.set(s, cnt + 1);
            }
        }

    }

    add(index: number, val: number): void {
        const tmp: number = this.nums2[index];
        this.nums2[index] += val;

        for (const n1 of this.nums1) {
            const oldSum: number = tmp + n1;
            const oldCnt: number = this.countBySum.get(oldSum) || 0;
            this.countBySum.set(oldSum, oldCnt - 1);

            const newSum: number = this.nums2[index] + n1;
            const newCnt: number = this.countBySum.get(newSum) || 0;
            this.countBySum.set(newSum, newCnt + 1);
        }

        return null;
    }

    count(tot: number): number {
        return (this.countBySum.get(tot) || 0);
    }
}

class FindSumPairs {
    nums1: number[];
    nums2: number[];
    countNum2: Map<number, number>;

    constructor(nums1: number[], nums2: number[]) {
        this.nums1 = nums1;
        this.nums2 = nums2;
        this.countNum2 = new Map();

        for (const n2 of this.nums2 ) {
            const cnt: number = this.countNum2.get(n2) || 0;
            this.countNum2.set(n2, cnt + 1);
        }

    }

    add(index: number, val: number): void {
        let cnt: number = this.countNum2.get(this.nums2[index]) || 0;
        this.countNum2.set(this.nums2[index], cnt - 1);

        this.nums2[index] += val;
        cnt = this.countNum2.get(this.nums2[index]) || 0;
        this.countNum2.set(this.nums2[index], cnt + 1);

    }

    count(tot: number): number {
        let count: number = 0;

        for (const n1 of this.nums1) {
            const diff: number = tot - n1;
            count += (this.countNum2.get(diff) || 0);
        }

        return count;
    }
}


const test = () => {
    const params = [
        {
            input: {
                commands: ["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"],
                params: [[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]],
            },
            output: [null, 8, null, 2, 1, null, null, 11],
        },
    ];

    params.forEach(({ input, output }) => {
        const { commands, params } = input;

        const findSumPairs = new FindSumPairs(params[0][0] as number[], params[0][1] as number[]);

        for (let i: number = 1; i < commands.length; ++i) {

            const result = commands[i] === 'count'
                ? findSumPairs.count(params[i][0] as number)
                : findSumPairs.add(params[i][0] as number, params[i][1] as number);

            console.log(
                JSON.stringify(result) === JSON.stringify(output[i])
                    ? "SUCCESS "
                    : "ERROR ",
                "input", JSON.stringify(commands[i]),
                "output", output[i],
                "result", result,
            );
        }


    });
};

test();
