/**
 * @param {string[]} words
 * @return {number}
 */
var countPrefixSuffixPairs = function(words) {
    const isPrefixAndSuffix = (w1, w2) => {
        if (w1.length > w2.length) {
            return false;
        }
        if (w1 === w2) {
            return true;
        }
        const pref = w2.slice(0, w1.length);
        const suff = w2.slice(w2.length - w1.length);

        return w1 === pref && w1 === suff;
    };

    let res = 0;

    for (let i = 0; i < words.length; ++i) {
        for (let j = i + 1; j < words.length; ++j) {
            if (isPrefixAndSuffix(words[i], words[j])) {
                res += 1;
            }
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: ['a','aba','ababa','aa'],
            output: 4,
        },
        {
            input: ['pa','papa','ma','mama'],
            output: 2,
        },
    ];

    params.forEach(({input, output}) => {
        const result = countPrefixSuffixPairs(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();