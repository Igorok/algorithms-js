/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function(text1, text2) {
    const dp = new Array(text1.length + 1).fill(0).map(() => new Array(text2.length + 1).fill(0))

    for (let i = 1; i <= text1.length; ++i) {
        for (let j = 1; j <= text2.length; ++j) {
            let val = Math.max(dp[i-1][j], dp[i][j-1]);
            if (text1[i - 1] === text2[j - 1]) {
                val = Math.max(dp[i-1][j-1] + 1, val);
            }
            dp[i][j] = val;
        }
    }



    return dp[text1.length][text2.length];
};

/*

  a b c d e
a
c
e



  a b c d e
a 1 1 1 1 1
c 1 1 2 2 2
e 1 1 2 2 3

  a b c d e
c 0 0 1 1 1
c 0 0 1 1 1
e 0 0 1 1 2
e 0 0 1 1 2


*/


const test = () => {
    const params = [
        {
            input: ["abcde", "ace" ],
            output: 3,
        },
        {
            input: ["abc", "abc"],
            output: 3,
        },
        {
            input: ["abc", "def"],
            output: 0,
        },
    ];

    for (const { input, output } of params) {
        const result = longestCommonSubsequence(...input);
        const message = `
            INPUT: ${JSON.stringify(input)}
            OUTPUT: ${output}
            RESULT: ${result}
            `;

        if (JSON.stringify(result) === JSON.stringify(output)) {
            console.log(
                'SUCCESS: \n', message,
            );
        } else {
            console.error('ERROR: \n', message);
        }
    }
};

test();
