
var Trie = function() {
    this.head = {};
    this._insert = function (node, char) {
        if (node[char]) return node[char];

        node[char] = {};
        return node[char];
    };
};

/**
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    let node = this.head;

    for (const char of word) {
        node = this._insert(node, char);
    }
    this._insert(node, 'END');

    return null;
};

/**
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    let node = this.head;
    for (const char of word) {
        node = node[char];
        if (!node) return false;
    }
    return Boolean(node['END']);
};

/**
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    let node = this.head;
    for (const char of prefix) {
        node = node[char];
        if (!node) return false;
    }
    return true;
};

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */


/*
const a = ['Trie', 'insert', 'search', 'search', 'startsWith', 'insert', 'search'];
const b = [[], ['apple'], ['apple'], ['app'], ['app'], ['app'], ['app']];

const r = [];
for (let i = 0; i < a.length; ++i) {
    r.push([
        a[i], b[i][0],
    ]);
}
console.log(JSON.stringify(r));
*/

const test = () => {
    const params = [
        {
            input: [
                ['insert','apple'],
                ['search','apple'],
                ['search','app'],
                ['startsWith','app'],
                ['insert','app'],
                ['search','app'],
            ],
            output: [null, true, false, true, null, true],
        },
    ];

    for (const { input, output } of params) {
        const trie = new Trie();
        for (let i = 0; i < input.length; ++i) {
            const [fn, str] = input[i];
            const result = trie[fn](str);

            const message = `
                INPUT: ${JSON.stringify(input[i])}
                OUTPUT: ${output[i]}
                RESULT: ${result}
                `;

            if (result === output[i]) {
                console.log(
                    'SUCCESS: \n', message,
                );
            } else {
                console.error('ERROR: \n', message);
            }
        }


    }
};

test();
