/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    const prefixTree = {};
    for (const word of wordDict) {
        let node = prefixTree;
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

    let visited = {};
    let node = prefixTree;
    let ends = [];
    let i = 0;
    while (i < s.length) {
        const char = s[i];
        if (!node[char] || (i === s.length - 1 && !node[char]['END'])) {
            if (!ends.length) {
                return false;
            }
            i = ends.pop();
            if (visited[i]) {
                return false;
            }
            visited[i] = 1;
            node = prefixTree;
        } else {
            if (node[char]['END']) {
                ends.push(i+1);
            }

            node = node[char];
            i += 1;
        }
    }

    return true;
};

const test = () => {
    const params = [
        {
            input: ["leetcode", ["leet","code"]],
            output: true,
        },
        {
            input: ["applepenapple", ["apple","pen"]],
            output: true,
        },
        {
            input: ["catsandog", ["cats","dog","sand","and","cat"]],
            output: false,
        },
        {
            input: ["dogsand", [ "sand","dog",]],
            output: true,
        },
        {
            input: ["aaaaaa", [ "a","aa","aaa"]],
            output: true,
        },
        {
            input: ["leetcode", ["leet","leetcode"]],
            output: true,
        },
        {
            input: ["leetcoder", ["leet","leetcode", "coder"]],
            output: true,
        },
        {
            input: ["aaaaaaa", ["aaaa","aa"]],
            output: false,
        },
        {
            input: ["bb", ["a","b","bbb","bbbb"]],
            output: true,
        },
        {
            input: ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]],
            output: true,
        },
    ];

    params.forEach(({input, output}) => {
        const result = wordBreak(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();