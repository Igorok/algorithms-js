function isScramble_0(s1: string, s2: string): boolean {
    const a1: string = s1.split('').sort().join('');
    const a2: string = s2.split('').sort().join('');
    if (a1 !== a2) {
        return false;
    }

    // const cache = new Map();
    const rec = (acc: string[]): boolean => {
        const key: string = acc.join('_');
        // if (cache.has(key)) {
        //     return cache.get(key);
        // }

        if (acc.join('') === s2) {
            // cache.set(key, true);
            return true;
        }

        for (let i: number = 0; i < acc.length; ++i) {
            if (acc[i].length === 1) {
                continue;
            }

            const left: string[] = acc.slice(0, i);
            const leftChars = left.join('').split('').sort().join('');
            const leftTarget = s2.slice(0, leftChars.length).split('').sort().join('');
            if (leftChars !== leftTarget) {
                // cache.set(key, false);
                return false;
            }

            const right: string[] = acc.slice(i+1);
            const rightChars = right.join('').split('').sort().join('');
            const rightTarget = s2.slice(s2.length - rightChars.length).split('').sort().join('');
            if (rightChars !== rightTarget) {
                // cache.set(key, false);
                return false;
            }

            const middleChars: string = acc[i].split('').sort().join('');
            const middleTarget: string = s2.slice(
                leftChars.length,
                s2.length - rightChars.length,
            ).split('').sort().join('');
            if (middleChars !== middleTarget) {
                // cache.set(key, false);
                return false;
            }

            for (let j = 1; j < acc[i].length; ++j) {
                let first: string = acc[i].slice(0, j);
                let second: string = acc[i].slice(j);

                let firstChars: string = first.split('').sort().join('');
                let firstTarget: string = s2.slice(leftChars.length, s2.length - rightChars.length - second.length).split('').sort().join('');

                let secondChars: string = second.split('').sort().join('');
                let secondTarget: string = s2.slice(leftChars.length + firstChars.length, s2.length - rightChars.length).split('').sort().join('');

                if (firstChars === firstTarget && secondChars === secondTarget) {
                    const r: boolean = rec([
                        ...left,
                        ...[first, second],
                        ...right,
                    ]);

                    if (r) return r;
                }

                let first1: string = second;
                let second1: string = first;

                firstChars = first1.split('').sort().join('');
                firstTarget = s2.slice(leftChars.length, s2.length - rightChars.length - second1.length ).split('').sort().join('');

                secondChars = second1.split('').sort().join('');
                secondTarget = s2.slice(leftChars.length + firstChars.length, s2.length - rightChars.length).split('').sort().join('');

                if (firstChars === firstTarget && secondChars === secondTarget) {
                    const r: boolean = rec([
                        ...left,
                        ...[second, first],
                        ...right,
                    ]);

                    if (r) return r;
                }
            }
        }

        // cache.set(key, false);
        return false;
    };


    return rec([s1]);
};



function isScramble(s1: string, s2: string): boolean {
    const cache = new Map();

    const rec = (str: string, target: string) => {
        if (str === target) {
            return true;
        }
        if (str.length === 1) {
            return false;
        }

        const key: string = [str, target].join('_');
        if (cache.has(key)) {
            return cache.get(key);
        }

        const charsStr = str.split('').sort().join('');
        const charsTarget = target.split('').sort().join('');

        if (charsStr !== charsTarget) {
            return false;
        }

        let res: boolean = false;
        for (let i = 1; i < str.length; ++i) {
            const left: string = str.slice(0, i);
            const right: string = str.slice(i);

            res = rec(left, target.slice(0, i)) && rec(right, target.slice(i));
            if (res) {
                break;
            }

            res = rec(left, target.slice(target.length - left.length)) && rec(right, target.slice(0, right.length));
            if (res) {
                break;
            }
        }

        cache.set(key, res);

        return res;
    };

    return rec(s1, s2);
};
/*
s1: "great", s2: "rgeat"
great
rgeat


s1: "abcde", s2: "caebd"



*/

const test = () => {
    const params = [
        {
            input: { s1: "abc", s2: "acb" },
            output: true,
        },
        {
            input: { s1: "great", s2: "rgeat" },
            output: true,
        },
        {
            input: { s1: "abcde", s2: "caebd" },
            output: false,
        },
        {
            input: { s1: "a", s2: "a" },
            output: true,
        },
        {
            input: { s1: "abcdbdacbdac", s2: "bdacabcdbdac" },
            output: true,
        },
        {
            input: { s1: "abcdefghijklmnopq", s2: "efghijklmnopqcadb" },
            output: false,
        },
        {
            input: { s1: "eebaacbcbcadaaedceaaacadccd", s2: "eadcaacabaddaceacbceaabeccd" },
            output: false,
        },
    ];

    params.forEach(({input, output}) => {
        const { s1, s2 } = input;

        const result = isScramble(s1, s2);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();