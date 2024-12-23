/**
 * @param {string} key
 * @param {string} message
 * @return {string}
 */
var decodeMessage = function(key, message) {
    const chars = new Map();
    for (let i = 0; i < key.length; ++i) {
        if (chars.size === 26) break;
        if (key[i] === ' ' || chars.has(key[i])) continue;

        const val = String.fromCharCode('a'.charCodeAt() + chars.size);
        chars.set(key[i], val);
    }

    const res = [];
    for (const char of message) {
        if (char === ' ') {
            res.push(' ');
        } else {
            res.push(chars.get(char));
        }
    }

    return res.join('');
};

const test = () => {
    const params = [
        {
            input: ["the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"],
            output: 'this is a secret',
        },
        {
            input: ["eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"],
            output: 'the five boxing wizards jump quickly',
        },
    ];

    for (const { input, output } of params) {
        const result = decodeMessage(...input);
        const message = `
            INPUT: ${input}
            OUTPUT: ${output}
            RESULT: ${result}
            `;

        if (result === output) {
            console.log(
                'SUCCESS: \n', message,
            );
        } else {
            console.error('ERROR: \n', message);
        }
    }
};

test();
