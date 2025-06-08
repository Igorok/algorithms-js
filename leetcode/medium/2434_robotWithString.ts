function robotWithString(s: string): string {
    const minSCodes: number[] = new Array(s.length).fill(0);
    minSCodes[minSCodes.length - 1] = s.charCodeAt(s.length - 1);

    for (let i: number = s.length - 2; i > -1; --i) {
        const iCode: number = s.charCodeAt(i);
        minSCodes[i] = Math.min(iCode, minSCodes[i + 1]);
    }

    const robot: string[] = [];
    const result: string[] = [];

    for (let i: number = 0; i < s.length; ++i) {
        while (robot.length && robot.at(-1).charCodeAt(0) <= minSCodes[i]) {
            result.push(robot.pop());
        }

        robot.push(s[i]);
    }

    while (robot.length) {
        result.push(robot.pop());
    }

    return result.join('');
};

/*

ERROR  input "vzhofnpo" output fnohopzv result fohnopzv

abcabc
bc bc
aa

*/

const test = () => {
    const params = [
        {
            input: "abcabc",
            output: 'aabcbc',
        },
        {
            input: "bac",
            output: 'abc',
        },
        {
            input: "zza",
            output: 'azz',
        },
        {
            input: "bdda",
            output: 'addb',
        },
        {
            input: "vzhofnpo",
            output: 'fnohopzv',
        },
    ];

    params.forEach(({input, output}) => {
        const result = robotWithString(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();