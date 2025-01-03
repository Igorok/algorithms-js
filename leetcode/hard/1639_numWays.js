/**
 * @param {string[]} words
 * @param {string} target
 * @return {number}
 */
var numWays = function(words, target) {
    const tLength = target.length;
    const wLength = words[0].length;
    const remainder = 7 + 10e8;

    const charsCount = new Array(wLength).fill(0).map(() => new Array(26).fill(0));
    const aCode = 'a'.charCodeAt();
    for (const word of words) {
        for (let i = 0; i < word.length; ++i) {
            const code = word[i].charCodeAt();
            charsCount[i][code - aCode] += 1;
        }
    }

    const cache = new Array(tLength).fill(0).map(() => new Array(wLength).fill(-1));
    const rec = (tId, wId) => {
        if (tLength - tId > wLength - wId) {
            return 0;
        }
        if (tId === tLength) {
            return 1;
        }
        if (cache[tId][wId] !== -1) {
            return cache[tId][wId];
        }

        const code = target[tId].charCodeAt();
        let totalResult = 0;
        // I can multiply the result on 3, instead of launching recursion 3 times
        if (charsCount[wId][code - aCode]) {
            totalResult = rec(tId + 1, wId + 1);
            totalResult *= charsCount[wId][code- aCode];
        }
        totalResult += rec(tId, wId + 1);
        totalResult %= remainder;

        cache[tId][wId] = totalResult

        return totalResult;
    };

    return rec(0, 0);
};

const test = () => {
    const params = [
        {
            input: [['acca','bbbb','caca'], 'aba'],
            output: 6,
        },
        {
            input: [['abba','baab'], 'bab'],
            output: 4,
        },
    ];

    params.forEach(({input, output}) => {
        const result = numWays(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();