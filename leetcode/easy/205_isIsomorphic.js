/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    const charsMap1 = new Map();
    const charsMap2 = new Map();

    for (let i = 0; i < s.length; ++i) {
        const char1 = s[i];
        const char2 = t[i];

        if (!charsMap1.has(char1)) {
            charsMap1.set(char1, char2);
        } else if (charsMap1.get(char1) !== char2) {
            return false;
        }

        if (!charsMap2.has(char2)) {
            charsMap2.set(char2, char1);
        } else if (charsMap2.get(char2) !== char1) {
            return false;
        }
    }

    return true;
};

var test = function () {
    var params = [
        {
            input: ['egg', 'add'],
            output: true,
        },
        {
            input: ['foo', 'bar'],
            output: false,
        },
        {
            input: ['paper', 'title'],
            output: true,
        },
    ];

    params.forEach(({input, output}) => {
        const result = isIsomorphic(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};
test();
