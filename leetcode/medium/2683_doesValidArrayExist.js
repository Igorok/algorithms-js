/**
 * @param {number[]} derived
 * @return {boolean}
 */
var doesValidArrayExist_0 = function(derived) {
    const sum  = derived.reduce((acc, num) => (num + acc), 0);
    return !Boolean(sum % 2);
};

var doesValidArrayExist = function(derived) {
    // 1,0,1,0,0,0,0,0,0
    // 1 0 0 1 1 1 1 1 1

    // 0 1 1
    // 0 0 1
    // 1 1 0

    // 1 1 0
    // 1 0 1 1

    // 1 0 1
    // 1 0 0

    return Boolean((derived.reduce((acc, num) => (num + acc), 0) + 1) % 2);
};

/*

---
1,1,0
1 0 1
0 1 0

1 1
1 0
0 1

1 0
0 1 -
1 0 -


1,0,1,0,0,0,0,0,0
1 0 0 1 1 1 1 1 1

1,0,1,0,1,0,0,0,0
0 1 1 0 0 0 0 0 0


---


*/

const test = () => {
    const params = [
        {
            input: [1,1,0],
            output: true,
        },
        {
            input: [1,1],
            output: true,
        },
        {
            input: [1,0],
            output: false,
        },
        {
            input: [1,0,1,0,0,0,0,0,0],
            output: true,
        },
    ];

    for (const { input, output } of params) {
        const result = doesValidArrayExist(input);
        const message = `
            INPUT: ${JSON.stringify(input)}
            OUTPUT: ${JSON.stringify(output)}
            RESULT: ${JSON.stringify(result)}`;

        if (JSON.stringify(result) === JSON.stringify(output)) {
            console.log(
                `SUCCESS: ${message}`,
            );
        } else {
            console.error(`ERROR: ${message}`);
        }
    }
};

test();
