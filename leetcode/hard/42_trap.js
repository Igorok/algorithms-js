/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let res = 0;
    let left = 0;

    for (let i = 1; i < height.length; ++i) {
        if (height[i] >= height[left] || i === height.length - 1) {
            let minBorder = Math.min(height[left], height[i]);
            for (let j = i - 1; j > left; --j) {
                minBorder = Math.max(minBorder, height[j]);
                res += Math.max(minBorder-height[j], 0);
            }
            left = i;
        }
    }

    return res;
};

/*


[0,1,0,2,1,0,1,3,2,1,2,1]

0,1,0,2,1,0,1,3,2,1,2,1
0 1 = 0
  1 0 2 = 1
      2 1 0 1 3 = 1 + 2 + 1 = 4
              3 2 1 2 1 = 1
0+1+4+1=6


[4,2,0,3,2,5]
4 2 0 3 2 5 = 2+4+1+2=9

2 1 0 1 2
1+2+1=4

2 1 0 1 2
2 1 0 1
=1
2 1 1
2 1 1 2
2 2
=1+2=3

2 1 0 1 2
min=2

3 2 1 0



*/






const test = () => {
    const params = [
        {
            input: [0,1,0,2,1,0,1,3,2,1,2,1],
            output: 6,
        },
        {
            input: [4,2,0,3,2,5],
            output: 9,
        },
    ];

    params.forEach(({input, output}) => {
        const result = trap(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();