/**
 * @param {string[]} words
 * @return {number}
 */
var countPrefixSuffixPairs_0 = function(words) {
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


var countPrefixSuffixPairs = function(words) {
    class Node {
        pref;
        suff;
        count = 1;
        children = {};

        constructor(pref, suff) {
            this.pref = pref;
            this.suff = suff;
        }

        getKey(pref, suff) {
            return [pref, suff].join('_');
        }

        insert(pref, suff) {
            const key = this.getKey(pref, suff);
            if (!this.children[key]) {
                this.children[key] = new Node(pref, suff);
            } else {
                this.children[key].count += 1;
            }

            return this.children[key];
        }

        getChild(pref, suff) {
            const key = this.getKey(pref, suff);
            return this.children[key];
        }
    };

    class Trie {
        root;

        constructor() {
            this.root = new Node('', '');
        }

        getWords(s) {
            const word = Array.from(s);
            const reversed = [...word].reverse();
            return [word, reversed];
        }

        count(s) {
            const [word, reversed] = this.getWords(s);
            let node = this.root;
            for (let i = 0; i < word.length; ++i) {
                node = node.getChild(word[i], reversed[i]);
                if (!node) {
                    return 0;
                }
            }
            return node.count;
        }

        insert(s) {
            const [word, reversed] = this.getWords(s);
            let node = this.root;
            for (let i = 0; i < word.length; ++i) {
                node = node.insert(word[i], reversed[i]);
            }
        }
    };

    const trie = new Trie();
    let res = 0;

    for (let i = words.length - 1; i > -1; --i) {
        res += trie.count(words[i]);
        trie.insert(words[i]);
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
        {
            input: ['abab','ab'],
            output: 0,
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