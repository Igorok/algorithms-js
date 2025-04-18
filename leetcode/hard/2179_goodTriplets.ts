class BIT {
    private sums: number [];
    constructor (length: number) {
        this.sums = new Array(length + 1).fill(0);
    }
    public query (id: number): number {
        let sum: number = 0;
        let i: number = id + 1;
        while (i > 0) {
            sum += this.sums[i];
            i -= i & (-i);
        }
        return sum;
    }
    public update (id: number, val: number): void {
        let i: number = id + 1;

        while (i < this.sums.length) {
            this.sums[i] += val;
            i += i & (-i);
        }
    }
};

function goodTriplets(nums1: number[], nums2: number[]): number {
    let res: number = 0;

    const idByVal1 = new Array(nums1.length).fill(0);
    for (let i = 0; i < nums1.length; ++i) {
        const val: number = nums1[i];
        idByVal1[val] = i;
    }

    const id1ForVal2 = new Array(nums1.length).fill(0);
    for (const val of nums2) {
        const id1 = idByVal1[val];
        id1ForVal2[val] = id1;
    }

    const bit: BIT = new BIT(nums1.length);

    for (let id2 = 0; id2 < nums2.length; ++id2) {
        const val2: number = nums2[id2];
        const id1: number = id1ForVal2[val2];

        const sumLeftIds1: number = bit.query(id1);
        bit.update(id1, 1);

        const insertedRightIds1: number = id2 - sumLeftIds1;
        const totalRightIds1: number = nums1.length - id1 - 1;
        const actualRightIds: number = totalRightIds1 - insertedRightIds1;

        res += sumLeftIds1 * actualRightIds;
    }

    return res;
};

/*
0 1 2 3 4
4,0,1,3,2
4,1,0,2,3

*/

const test = () => {
    const params = [
        {
            input: [[2,0,1,3], [0,1,2,3]],
            output: 1,
        },
        {
            input: [[4,0,1,3,2], [4,1,0,2,3]],
            output: 4,
        },
    ];

    params.forEach(({input, output}) => {
        const nums1: number[] = input[0] as number[];
        const nums2: number[] = input[1] as number[];
        const result = goodTriplets(nums1, nums2);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();