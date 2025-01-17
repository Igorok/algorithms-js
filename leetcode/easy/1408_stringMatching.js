/**
 * @param {string[]} words
 * @return {string[]}
 */
var stringMatching_0 = function(words) {
    const str = words.join('_');

    const res = [];
    for (const word of words) {
        const match = str.match(new RegExp(word, 'g'));
        if (match?.length > 1) {
            res.push(word);
        }
    }

    return res;
};

/*

30

*/

var stringMatching = function(words) {
    const p = 2;
    const str = words.join(' ');
    const mod = 7 + 10e7;
    const aCode = 'a'.charCodeAt();
    const codes = {};
    const getCharCode = (char, pow) => {
        const key = [char, pow].join('_');
        if (codes[key]) {
            return codes[key];
        }
        const code = char.charCodeAt() - aCode + 1;
        const m = (Math.pow(p, pow) % mod);
        codes[key] = ((code * m) % mod);
        return codes[key];
    }
    const getHash = (word, s, e) => {
        const p = e - s;
        let hash = 0;
        for (let i = e; i > s - 1; --i) {
            hash += getCharCode(word[i], p - i);
            hash %= mod;
        }
        return hash;
    };

    const res = [];
    for (const word of words) {
        const length = word.length - 1;
        const wordHash = getHash(word, 0, length);
        let startHash = 0;
        let count = 0;

        for (let i = 0; i < (str.length - length); ++i) {
            if (i === 0) {
                startHash = getHash(str, 0, length);
            } else {
                const lastChar = getCharCode(str[i - 1], length);
                const newChar = getCharCode(str[i + length], 0);

                startHash = (mod + startHash - lastChar);
                startHash *= p;
                startHash %= mod;
                startHash += newChar;
                startHash %= mod;
            }

            if (wordHash === startHash && word === str.slice(i, (i + word.length))) {
                count += 1;
                if (count === 2) {
                    res.push(word);
                    break;
                }
            }
        }
    }

    return res;
};


const test = () => {
    const params = [
        {
            input: ['mass','as','hero','superhero'],
            output: ['as','hero'],
        },
        {
            input: ['leetcode','et','code'],
            output: ['et','code'],
        },
        {
            input: ['leetcoder','leetcode','od','hamlet','am'],
            output: ['leetcode','od','am'],
        },
        {
            input: ['uexk','aeuexkf','wgxih','yuexk','gxea','yuexkm','ypmfx','jjuexkmb','wqpri','aeuexkfpo','kqtnz','pkqtnza','nrbb','hmypmfx','krqs','jjuexkmbyt','zvru','ypmfxj'],
            output: ['uexk','aeuexkf','yuexk','ypmfx','jjuexkmb','kqtnz'],
        },
        {
            input: ["bncaxjlwsxsem","afbncaxjlwsxsemue","ayjymfcsgqh","isayjymfcsgqhh","cyzwlgxe","disayjymfcsgqhh","rgjkzux","nxafbncaxjlwsxsemue","rezuexuxqfq","ddisayjymfcsgqhh","h","bncaxjlwsxsemw","uupu","disayjymfcsgqhhq","gjlysgj","cyzwlgxed","fuxcewqpmrmf","vmnxafbncaxjlwsxsemueqh","vtmuchhqfgzqz","mha","cho","fgjlysgjy","nfgojmffb","rsvtmuchhqfgzqzv","ipqzqmzm","itmhacy","lxnty","fnxafbncaxjlwsxsemue","plvhqyidqvfe","ofgjlysgjy","tyyhodyjaijrthwc","bncaxjlwsxseml","zsnmtb","mfgjlysgjy","yonmn","qrvmnxafbncaxjlwsxsemueqhb","vdhgnpkce","jgbncaxjlwsxsemr","rdfylztnqfjtmrb","rgjkzuxe","dp","aqjgbncaxjlwsxsemr","ohexxrowckqmg","ipqzqmzmgl","kdeqdzuceg","qnmfgjlysgjyzh","tfdtjiedjvjv","cfuxcewqpmrmf","ymwdp","qitmhacyp","c","qafbncaxjlwsxsemuea","p","ovmnxafbncaxjlwsxsemueqhx","yulr","pjcfuxcewqpmrmf","reahco","rbjgbncaxjlwsxsemrou","vxh","kwcyzwlgxednl"],
            output: ["bncaxjlwsxsem","afbncaxjlwsxsemue","ayjymfcsgqh","isayjymfcsgqhh","cyzwlgxe","disayjymfcsgqhh","rgjkzux","nxafbncaxjlwsxsemue","h","gjlysgj","cyzwlgxed","fuxcewqpmrmf","vmnxafbncaxjlwsxsemueqh","vtmuchhqfgzqz","mha","fgjlysgjy","ipqzqmzm","itmhacy","mfgjlysgjy","jgbncaxjlwsxsemr","dp","cfuxcewqpmrmf","c","p"],
        },
    ];

    params.forEach(({input, output}) => {
        const result = stringMatching(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();