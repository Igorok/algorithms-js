/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum_0 = function(nums) {
    const data = nums.sort((a, b) => a - b);
    const visited = {};
    const res = {};

    const rec = (i1, i2, i3) => {
        if (visited[[i1, i2, i3].join('_')]) return;

        visited[`${i1}_${i2}_${i3}`] = 1;
        const sum = data[i1] + data[i2] + data[i3];
        if (sum > 0) {
            return;
        }
        if (sum === 0) {
            const arr = [data[i1], data[i2], data[i3]].sort((a, b) => a - b);
            const key = arr.join('_');
            res[key] = arr;
        }

        if (i3 + 1 < data.length) {
            rec(i1, i2, i3 + 1);
        }
        if (i2 + 1 < i3) {
            rec(i1, i2+1, i3);
        }
        if (i1 + 1 < i2) {
            rec(i1+1, i2, i3);
        }
    };

    rec(0, 1, 2);

    return Object.values(res);
};


var threeSum_2 = function(nums) {
    const data = nums.sort((a, b) => a - b);
    const visited = {};
    const res = {};

    const rec = (i1, i3) => {
        const key = [i1, i3].join('_');
        if (visited[key]) return;

        visited[key] = 1;
        if (data[i1] > 0 || data[i3] < 0) {
            return;
        }

        const sum = data[i1] + data[i3];
        let start = i1 + 1;
        let end = i3 - 1;

        while (start <= end) {
            const m = Math.floor((start + end) / 2);
            if (sum + data[m] === 0) {
                const arr = [data[i1], data[m], data[i3]];
                const key = arr.join('_');
                res[key] = arr;
                break;
            } else if (sum + data[m] < 0) {
                start = m + 1;
            } else {
                end = m - 1;
            }
        }

        const tmp1 = i1;
        const tmp3 = i3;
        while (i1 < i3 - 1 && data[i1] === data[tmp1]) {
            i1 += 1;
        }
        while (i1 < i3 - 1 && data[i3] === data[tmp3]) {
            i3 -= 1;
        }
        rec(i1, tmp3);
        rec(tmp1, i3);
    };

    rec(0, data.length - 1);

    return Object.values(res);
};

var threeSum = function(nums) {
    const numbers = nums.sort((a, b) => a - b);

    let i = 0;
    let res = [];
    while (i < numbers.length - 2) {
        let left = i + 1;
        let right = numbers.length - 1;

        while (left < right) {
            if (numbers[i] + numbers[left] + numbers[right] === 0) {
                res.push([numbers[i], numbers[left], numbers[right]]);
                const v = numbers[left];
                while (left < right && numbers[left] === v) {
                    left += 1;
                }
            } else if (numbers[i] + numbers[left] + numbers[right] > 0) {
                const v = numbers[right];
                while (left < right && numbers[right] === v) {
                    right -= 1;
                }
            } else {
                const v = numbers[left];
                while (left < right && numbers[left] === v) {
                    left += 1;
                }
            }
        }

        const v = numbers[i];
        while (v === numbers[i] && i < numbers.length) {
            i += 1;
        }
    }

    return res;
};

/*
-1,0,1,2,-1,-4
-4,-1,-1,0,1,2

-2,-1,-1,-1,-1,0,1,1,1,3

-1,-1,-1,-1,-1,0,1,1,1,2


*/
const test = () => {
    const params = [
        // {
        //     input: [-1,0,1,2,-1,-4],
        //     output: [[-1,-1,2],[-1,0,1]],
        // },
        // {
        //     input: [0,1,1],
        //     output: [],
        // },
        // {
        //     input: [0,0,0],
        //     output: [[0,0,0]],
        // },
        {
            input: [-6,-5,-5,-4,9,10],
            output: [[-6,-4, 10],[-5,-5, 10], [-5,-4, 9]],
        },
        {
            input: [0,8,2,-9,-14,5,2,-5,-5,-9,-1,3,1,-8,0,-3,-12,2,11,9,13,-14,2,-15,4,10,9,7,14,-8,-2,-1,-15,-15,-2,8,-3,7,-12,8,6,2,-12,-8,1,-4,-3,5,13,-7,-1,11,-13,8,4,6,3,-2,-2,3,-2,3,9,-10,-4,-8,14,8,7,9,1,-2,-3,5,5,5,8,9,-5,6,-12,1,-5,12,-6,14,3,5,-11,8,-7,2,-12,9,8,-1,9,-1,-7,1,-7,1,14,-3,13,-4,-12,6,-9,-10,-10,-14,7,0,13,8,-9,1,-2,-5,-14],
            output: [[-15,1,14],[-15,2,13],[-15,3,12],[-15,4,11],[-15,5,10],[-15,6,9],[-15,7,8],[-14,0,14],[-14,1,13],[-14,2,12],[-14,3,11],[-14,4,10],[-14,5,9],[-14,6,8],[-14,7,7],[-13,-1,14],[-13,0,13],[-13,1,12],[-13,2,11],[-13,3,10],[-13,4,9],[-13,5,8],[-13,6,7],[-12,-2,14],[-12,-1,13],[-12,0,12],[-12,1,11],[-12,2,10],[-12,3,9],[-12,4,8],[-12,5,7],[-12,6,6],[-11,-3,14],[-11,-2,13],[-11,-1,12],[-11,0,11],[-11,1,10],[-11,2,9],[-11,3,8],[-11,4,7],[-11,5,6],[-10,-4,14],[-10,-3,13],[-10,-2,12],[-10,-1,11],[-10,0,10],[-10,1,9],[-10,2,8],[-10,3,7],[-10,4,6],[-10,5,5],[-9,-5,14],[-9,-4,13],[-9,-3,12],[-9,-2,11],[-9,-1,10],[-9,0,9],[-9,1,8],[-9,2,7],[-9,3,6],[-9,4,5],[-8,-6,14],[-8,-5,13],[-8,-4,12],[-8,-3,11],[-8,-2,10],[-8,-1,9],[-8,0,8],[-8,1,7],[-8,2,6],[-8,3,5],[-8,4,4],[-7,-7,14],[-7,-6,13],[-7,-5,12],[-7,-4,11],[-7,-3,10],[-7,-2,9],[-7,-1,8],[-7,0,7],[-7,1,6],[-7,2,5],[-7,3,4],[-6,-5,11],[-6,-4,10],[-6,-3,9],[-6,-2,8],[-6,-1,7],[-6,0,6],[-6,1,5],[-6,2,4],[-6,3,3],[-5,-5,10],[-5,-4,9],[-5,-3,8],[-5,-2,7],[-5,-1,6],[-5,0,5],[-5,1,4],[-5,2,3],[-4,-4,8],[-4,-3,7],[-4,-2,6],[-4,-1,5],[-4,0,4],[-4,1,3],[-4,2,2],[-3,-3,6],[-3,-2,5],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-2,4],[-2,-1,3],[-2,0,2],[-2,1,1],[-1,-1,2],[-1,0,1],[0,0,0]],
        },



    ];

    params.forEach(({input, output}) => {
        const result = threeSum(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            '\n input', JSON.stringify(input),
            '\n output', JSON.stringify(output),
            '\n result', JSON.stringify(result),
        );
    });
};

test();