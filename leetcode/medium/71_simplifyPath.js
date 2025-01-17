/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function(path) {
    const arr = path.split('/');
    const stack = [];

    for (let i = 0; i < arr.length; ++i) {
        if (!arr[i].length || arr[i] === '.') {
            continue;
        }
        if (arr[i] === '..') {
            stack.pop();
            continue;
        }
        stack.push(arr[i]);
    }

    return '/' + stack.join('/');
};

const test = () => {
    const params = [
        {
            input: "/home/",
            output: "/home",
        },
        {
            input: "/home//foo/",
            output: "/home/foo",
        },
        {
            input: "/home/user/Documents/../Pictures",
            output:  "/home/user/Pictures",
        },
        {
            input: "/../",
            output: "/",
        },
        {
            input: "/.../a/../b/c/../d/./",
            output: "/.../b/d",
        },
    ];

    params.forEach(({input, output}) => {
        const result = simplifyPath(input);

        console.log(
            result === output ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();