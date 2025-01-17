/**
 * @param {string} s
 * @param {string} locked
 * @return {boolean}
 */
var canBeValid_0 = function(s, locked) {
    if (s.length % 2) {
        return false;
    }

    let unlocked = 0;
    let open = 0;
    for (let i = 0; i < s.length; ++i) {
        if (locked[i] === '0') {
            unlocked += 1;
            continue;
        }
        if (s[i] === '(') {
            open += 1;
            continue;
        }

        if (open !== 0) {
            open -= 1;
        } else if (unlocked !== 0) {
            unlocked -= 1;
        } else {
            return false;
        }
    }

    unlocked = 0;
    closed = 0;
    for (let i = s.length - 1; i > -1; --i) {
        if (locked[i] === '0') {
            unlocked += 1;
            continue;
        }
        if (s[i] === ')') {
            closed += 1;
            continue;
        }

        if (closed !== 0) {
            closed -= 1;
        } else if (unlocked !== 0) {
            unlocked -= 1;
        } else {
            return false;
        }
    }

    return true;
};



const test = () => {
    const params = [
        {
            input: ["))()))", "010100"],
            output: true,
        },
        {
            input: ["()()", "0000"],
            output: true,
        },
        {
            input: [")", "0"],
            output: false,
        },
        {
            input: ["))((", "0000"],
            output: true,
        },
        {
            input: ["))((", "1000"],
            output: false,
        },
        {
            input: ["((((", "0011"],
            output: false,
        },
        {
            input: ["(())", "0011"],
            output: true,
        },
        {
            input: ["(())))", "000111"],
            output: true,
        },
        {
            input: ["((((((", "001000"],
            output: true,
        },
    ];

    params.forEach(({input, output}) => {
        const result = canBeValid(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();


// ["dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg","ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"].length