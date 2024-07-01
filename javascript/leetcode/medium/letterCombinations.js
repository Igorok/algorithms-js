/**
 * https://leetcode.com/problems/letter-combinations-of-a-phone-number/
 *
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if (digits.length === 0) return [];

    const btns = {
        2: ['a','b','c'],
        3: ['d','e','f'],
        4: ['g','h','i'],
        5: ['j','k','l'],
        6: ['m','n','o'],
        7: ['p','q','r','s'],
        8: ['t','u','v'],
        9: ['w','x','y','z',],
    };
    const result = [];

    const getAllCases = (id, str = '') => {
        if (id === digits.length) {
            result.push(str);
            return;
        }

        const dg = digits[id];

        btns[dg].forEach((lt) => {
            getAllCases(id + 1, str + lt);
        });
    }

    getAllCases(0, '');

    return result;
};

console.log(
    '23', letterCombinations('23'),
    '', letterCombinations(''),
    '2', letterCombinations('2'),
);
