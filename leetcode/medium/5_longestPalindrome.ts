function longestPalindrome(s: string): string {
    let longest: number[] = [0,0];

    for (let i: number = 1; i < s.length; ++i) {
        let left: number = i;
        let right: number = i;

        while (left > -1 && right < s.length) {
            if (s[left] !== s[right]) {
                break;
            }

            if (right - left + 1 > longest[1] - longest[0] + 1) {
                longest = [left, right];
            }

            left -= 1;
            right += 1;
        }

        left = i;
        right = i-1;

        while (left > -1 && right < s.length) {
            if (s[left] !== s[right]) {
                break;
            }

            if (right - left + 1 > longest[1] - longest[0] + 1) {
                longest = [left, right];
            }

            left -= 1;
            right += 1;
        }
    }


    return s.slice(longest[0], longest[1] + 1);
};

const test = () => {
    const params = [

        {
            input: {
                s: "babad"
            },
            output: 'bab',
        },
        {
            input: {
                s: "cbbd"
            },
            output: 'bb',
        },
    ];

    params.forEach(({input, output}) => {
        const { s } = input;

        const result = longestPalindrome(s);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();