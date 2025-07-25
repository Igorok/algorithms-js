function minCut_0(s: string): number {
    const dfs = (str: string) => {
        if (str.length < 2) {
            return 0;
        }

        const reversed: string = str.split('').reverse().join('');
        if (str === reversed) {
            return 0;
        }

        let longest: number[] = [0,0];
        for (let i: number = 0; i < s.length; ++i) {
            for (let j: number = i+1; j < s.length; ++j) {
                const substr: string = str.slice(i, j+1);
                const reversed: string = substr.split('').reverse().join('');
                if (substr === reversed && (j-i+1) > (longest[1]-longest[0]+1)) {
                    longest = [i, j];
                }
            }
        }

        let res: number = 0;
        if (longest[0] > 0) {
            res += 1;
            res += dfs(str.slice(0, longest[0]));
        }
        if (longest[1] < str.length - 1) {
            res += 1;
            res += dfs(str.slice(longest[1]+1));
        }

        return res;
    }

    return dfs(s);
};


function minCut_1(s: string): number {
    const memo: Map<string, number> = new Map();

    const dfs = (left: number, right: number) => {
        if (right - left + 1 < 2) {
            return 0;
        }

        const key: string = [left, right].join('_');

        if (memo.has(key)) {
            return memo.get(key);
        }

        const substr: string = s.slice(left, right + 1);
        const reversed: string = substr.split('').reverse().join('');
        if (substr === reversed) {
            return 0;
        }

        let res: number = Number.MAX_SAFE_INTEGER;

        for (let i: number = left; i <= right; ++i ) {
            const substr: string = s.slice(left, i + 1);
            const reversed: string = substr.split('').reverse().join('');
            if (substr === reversed) {
                const r: number = 1 + dfs(i+1, right);

                res = Math.min(res, r);
            }
        }

        memo.set(key, res);

        return res;
    }

    return dfs(0, s.length-1);
};


function minCut_2(s: string): number {
    const count: number[] = new Array(s.length).fill(Number.MAX_SAFE_INTEGER);
    count[0] = 1;

    const isPalindrome = (left: number, right: number) => {
        while (left < right) {
            if (s[left] !== s[right]) {
                return false;
            }
            left += 1;
            right -= 1;
        }

        return true;
    }

    for (let i: number = 1; i < s.length; ++i) {
        for (let j = i; j > -1; --j) {
            if (isPalindrome(j, i)) {
                const leftCount: number = j > 0 ? count[j-1] : 0;
                count[i] = Math.min(count[i], leftCount + 1);
            }
        }
    }

    return count[s.length-1]-1;
};

function minCut(s: string): number {
    const count: number[] = new Array(s.length).fill(Number.MAX_SAFE_INTEGER);
    count[0] = 1;

    for (let i: number = 1; i < s.length; ++i) {
        // odd
        let left: number = i;
        let right: number = i;

        while (left > -1 && right < s.length) {
            if (s[left] !== s[right]) {
                break;
            }

            let leftCount: number = left === 0 ? 0 : count[left - 1];
            count[right] = Math.min(count[right], leftCount+1);

            right += 1;
            left -= 1;
        }

        // even
        left = i;
        right = i-1;

        while (left > -1 && right < s.length) {
            if (s[left] !== s[right]) {
                break;
            }

            let leftCount: number = left === 0 ? 0 : count[left - 1];
            count[right] = Math.min(count[right], leftCount+1);

            right += 1;
            left -= 1;
        }

    }

    return count[s.length-1]-1;

};


/*

aaaaba


*/

const test = () => {
    const params = [
        {
            input: {
                s: "ccaacabacb",
            },
            output: 3,
        },
        {
            input: {
                s: "aab",
            },
            output: 1,
        },

        {
            input: {
                s: "aaabaa",
            },
            output: 1,
        },
        {
            input: {
                s: "coder",
            },
            output: 4,
        },

        {
            input: {
                s: "a",
            },
            output: 0,
        },
        {
            input: {
                s: "ab",
            },
            output: 1,
        },
        {
            input: {
                s: "kwtbjmsjvbrwriqwxadwnufplszhqccayvdhhvscxjaqsrmrrqngmuvxnugdzjfxeihogzsdjtvdmkudckjoggltcuybddbjoizu",
            },
            output: 89,
        },
        {
            input: {
                s: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
            },
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const { s } = input;

        const result = minCut(s);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();