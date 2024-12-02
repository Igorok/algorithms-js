/**
 * @param {string[]} products
 * @param {string} searchWord
 * @return {string[][]}
 */
var suggestedProducts_1 = function(products, searchWord) {
    class PrefixTree {
        #prefixTree = {};

        constructor () {
            this.#prefixTree = {};
        }

        insert (word) {
            let node = this.#prefixTree;

            for (const char of word) {
                if (!node[char]) {
                    node[char] = {};
                }
                node = node[char];
            }

            if (!node['END']) {
                node['END'] = 'END';
            }
        }

        find (letters) {
            let node = this.#prefixTree;
            const result = [];

            for (const char of letters) {
                if (!node[char]) return [];

                node = node[char];
            }

            const stack = [];
            for (const k in node) {
                if (k === 'END') {
                    result.push(letters);
                } else {
                    stack.push([node[k], letters + k]);
                }
            }

            while (stack.length) {
                const [node, str] = stack.pop();
                for (const k in node) {
                    if (k === 'END') {
                        result.push(str);
                    } else {
                        stack.push([node[k], str + k]);
                    }
                }
            }

            return result.sort().slice(0, 3);
        }
    }

    const prefixTree = new PrefixTree();
    for (const product of products) {
        prefixTree.insert(product);
    }

    const res = [];
    for (let i = 1; i <= searchWord.length; ++i) {
        const r = prefixTree.find(searchWord.slice(0, i));
        res.push(r);
    }

    return res;
};

var suggestedProducts = function(products, searchWord) {
    class PrefixTree {
        #prefixTree = {};

        constructor () {
            this.#prefixTree = {};
        }

        insert (word) {
            let node = this.#prefixTree;

            for (const char of word) {
                if (!node[char]) {
                    node[char] = {};
                }
                node = node[char];
            }

            if (!node['END']) {
                node['END'] = 'END';
            }
        }

        find (letters) {
            let node = this.#prefixTree;
            const result = [];

            for (const char of letters) {
                if (!node[char]) return [];

                node = node[char];
            }

            const dfs = (node, str) => {
                if (result.length === 3) return;

                const keys = Object.keys(node).sort().slice(0, 3);
                for (const k of keys) {
                    if (k === 'END') {
                        result.push(str);
                    } else {
                        dfs(node[k], str + k);
                    }
                }
            }

            dfs(node, letters);

            return result.sort().slice(0, 3);
        }
    }

    const prefixTree = new PrefixTree();
    for (const product of products) {
        prefixTree.insert(product);
    }

    const res = [];
    for (let i = 1; i <= searchWord.length; ++i) {
        const r = prefixTree.find(searchWord.slice(0, i));
        res.push(r);
    }

    return res;
};

/*

ERROR
input
[["mobile","mouse","moneypot","monitor","mousepad"],"mouse"]

output
[
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]


result
[["monitor","moneypot","mouse"],["monitor","moneypot","mouse"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]











*/

const test = () => {
    const params = [
        {
            input: [["mobile","mouse","moneypot","monitor","mousepad"], "mouse"],
            output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]],
        },
        {
            input: [["havana"], "havana"],
            output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]],
        },

    ];

    params.forEach(({input, output}) => {
        const result = suggestedProducts(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();