function longestPalindrome(words: string[]): number {
    let maxOddPalindrome: string = '';
    const strCount: Map<string, number> = new Map();

    for (const word of words) {
        const count: number = (strCount.get(word) || 0) + 1;
        strCount.set(word, count);
    }

    strCount.forEach((count: number, word: string) => {
        const reversed: string = word.split('').reverse().join('');
        if (reversed === word && (count % 2) === 1) {
            if (maxOddPalindrome === '' || count > strCount.get(maxOddPalindrome)) {
                maxOddPalindrome = word;
            }
        }
    });

    let res: number = 0;
    const used: Set<string> = new Set();
    if (maxOddPalindrome !== '') {
        used.add(maxOddPalindrome);
        res = strCount.get(maxOddPalindrome) * 2;
    }

    strCount.forEach((count: number, word: string) => {
        if (used.has(word)) {
            return;
        }

        const reversed: string = word.split('').reverse().join('');
        used.add(word);
        if (reversed === word) {
            if (maxOddPalindrome !== '' && (count % 2) === 1) {
                res += (count-1) * 2;
                return;
            }
            res += count * 2;
            return;
        }

        used.add(reversed);

        res += Math.min(count, strCount.get(reversed) || 0) * 2 * 2;
    });


    return res;
};


/*

"nn","nn","hg","gn","nn","hh","gh","nn","nh","nh"

"gn","nh","nh"
"hg","nn","nn", "hh", "nn","nn","gh",




*/


const test = () => {
    const params = [
        {
            input: { words: ["lc","cl","gg"] },
            output: 6,
        },
        {
            input: { words: ["ab","ty","yt","lc","cl","ab"] },
            output: 8,
        },
        {
            input: { words: ["cc","ll","xx"] },
            output: 2,
        },
        {
            input: { words: ['cb', 'ba', 'ab', 'bc'] },
            output: 8,
        },
        {
            input: { words: ["nn","nn","hg","gn","nn","hh","gh","nn","nh","nh"] },
            output: 14,
        },
    ];

    params.forEach(({input, output}) => {
        const { words } = input;
        const result = longestPalindrome(words);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();