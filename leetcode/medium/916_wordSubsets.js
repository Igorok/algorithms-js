/**
 * @param {string[]} words1
 * @param {string[]} words2
 * @return {string[]}
 */
var wordSubsets_0 = function(words1, words2) {
    const res = [];

    for (const word of words1) {
        let isSubset = 0;
        for (const subset of words2) {
            let id = 0;
            for (const char of word) {
                if (char === subset[id]) {
                    id += 1;
                }
                if (id === subset.length) {
                    isSubset += 1;
                    break;
                }
            }
        }
        if (isSubset === words2.length) {
            res.push(word);
        }
    }

    return res;
};


var wordSubsets_1 = function(words1, words2) {
    const res = [];

    const getMap = (arr) => {
        const mapChar = new Map();

        for (const word of arr) {
            const count = {};
            for (const char of word) {
                count[char] = (count[char] || 0) + 1;
            }
            mapChar.set(word, count);
        }

        return mapChar;
    };

    const map1 = getMap(words1);
    const map2 = getMap(words2);

    const isSubset = (countWord) => {
        for (const countSubset of map2.values()) {
            for (const [char, count] of Object.entries(countSubset)) {
                if (!countWord[char] || countWord[char] < count) {
                    return false;
                }
            }
        }
        return true;
    };

    map1.forEach((countWord, word) => {
        if (isSubset(countWord)) {
            res.push(word);
        }
    });

    return res;
};

var wordSubsets = function(words1, words2) {
    const aCode = 'a'.charCodeAt();
    const charsCodes = new Array(26).fill(0);

    for (const subset of words2) {
        const chars = new Array(26).fill(0);

        for (const char of subset) {
            const code = char.charCodeAt() - aCode;
            chars[code] += 1;

            charsCodes[code] = Math.max(charsCodes[code], chars[code]);
        }
    }
    const charsCount = charsCodes.reduce((acc, num) => (acc + num), 0);

    const isSubset = (word) => {
        const charsArr = new Array(26).fill(0);
        let count = 0;

        for (let i = 0; i < word.length; ++i) {
            if (word.length - i < charsCount - count) {
                return false;
            }

            const code = word[i].charCodeAt() - aCode;
            if (charsCodes[code] > charsArr[code]) {
                charsArr[code] += 1;
                count += 1;
            }
        }

        return charsCount === count;
    }

    const res = [];

    for (const word of words1) {
        if (isSubset(word)) {
            res.push(word);
        }
    }

    return res;
};


const test = () => {
    const params = [
        {
            input: [['amazon','apple','facebook','google','leetcode'], ['e','o']],
            output: ['facebook','google','leetcode'],
        },
        {
            input: [['amazon','apple','facebook','google','leetcode'], ['l','e']],
            output: ['apple','google','leetcode'],
        },
        {
            input: [["amazon","apple","facebook","google","leetcode"], ["lo","eo"]],
            output: ["google","leetcode"],
        },
    ];

    params.forEach(({input, output}) => {
        const result = wordSubsets(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();