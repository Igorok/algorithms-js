

function findLadders(beginWord: string, endWord: string, wordList: string[]): string[][] {
    const adj: Map<string, string[]> = new Map();
    const visitedLayers: Map<string, number> = wordList.reduce((acc: Map<string, number>, word: string) => {
        acc.set(word, -1);
        return acc;
    }, new Map());

    const queue: string[] = [beginWord];
    visitedLayers.set(beginWord, 0);

    while (queue.length !== 0) {
        const word: string = queue.shift();
        const layer: number = visitedLayers.get(word);

        if (word === endWord) {
            break;
        }

        for (let i: number = 0; i < word.length; ++i) {
            const left: string = i === 0 ? '' : word.slice(0, i);
            const right: string = i === word.length - 1 ? '' : word.slice(i+1);

            for (let code: number = 97; code <= 122; ++code) {
                const char: string = String.fromCharCode(code);
                const newWord: string = left + char + right;

                if (char === word[i] || !visitedLayers.has(newWord)) {
                    continue;
                }

                const l: number = visitedLayers.get(newWord);
                if (l === -1) {
                    visitedLayers.set(newWord, layer + 1);
                    queue.push(newWord);
                    const nei: string[] = adj.get(word) || [];
                    nei.push(newWord);
                    adj.set(word, nei);
                }
                else if (l === layer + 1) {
                    const nei: string[] = adj.get(word) || [];
                    nei.push(newWord);
                    adj.set(word, nei);
                }
            }
        }
    }

    if (!visitedLayers.has(endWord)) {
        return [];
    }

    const memo: Map<string, string[][]> = new Map();

    const dfs = (word: string) => {
        if (word === endWord) {
            return [[word]];
        }

        if (memo.has(word)) {
            return memo.get(word);
        }

        if (visitedLayers.get(word) >= visitedLayers.get(endWord)) {
            return [];
        }

        const res: string[][] = [];
        const children: string[] = adj.get(word) || [];

        for (const nei of children) {
            const path: string[][] = dfs(nei);

            if (path.length !== 0) {
                for (const p of path) {
                    res.push([word, ...p]);
                }
            }
        }

        memo.set(word, res);
        return res;
    };


    return dfs(beginWord);
};






const test = () => {
    const params = [
        {
            input: {
                beginWord: "red",
                endWord: "tax",
                wordList: ["ted","tex","red","tax","tad","den","rex","pee"],
            },
            output: [["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]],
        },
        {
            input: {
                beginWord: "hit",
                endWord: "cog",
                wordList: ["hot","dot","dog","lot","log","cog"]
            },
            output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]],
        },
        {
            input: {
                beginWord: "hit",
                endWord: "cog",
                wordList: ["hot","dot","dog","lot","log"]
            },
            output: [],
        },

        {
            input: {
                beginWord: "aaaaa",
                endWord: "ggggg",
                wordList: ["aaaaa","caaaa","cbaaa","daaaa","dbaaa","eaaaa","ebaaa","faaaa","fbaaa","gaaaa","gbaaa","haaaa","hbaaa","iaaaa","ibaaa","jaaaa","jbaaa","kaaaa","kbaaa","laaaa","lbaaa","maaaa","mbaaa","naaaa","nbaaa","oaaaa","obaaa","paaaa","pbaaa","bbaaa","bbcaa","bbcba","bbdaa","bbdba","bbeaa","bbeba","bbfaa","bbfba","bbgaa","bbgba","bbhaa","bbhba","bbiaa","bbiba","bbjaa","bbjba","bbkaa","bbkba","bblaa","bblba","bbmaa","bbmba","bbnaa","bbnba","bboaa","bboba","bbpaa","bbpba","bbbba","abbba","acbba","dbbba","dcbba","ebbba","ecbba","fbbba","fcbba","gbbba","gcbba","hbbba","hcbba","ibbba","icbba","jbbba","jcbba","kbbba","kcbba","lbbba","lcbba","mbbba","mcbba","nbbba","ncbba","obbba","ocbba","pbbba","pcbba","ccbba","ccaba","ccaca","ccdba","ccdca","cceba","cceca","ccfba","ccfca","ccgba","ccgca","cchba","cchca","cciba","ccica","ccjba","ccjca","cckba","cckca","cclba","cclca","ccmba","ccmca","ccnba","ccnca","ccoba","ccoca","ccpba","ccpca","cccca","accca","adcca","bccca","bdcca","eccca","edcca","fccca","fdcca","gccca","gdcca","hccca","hdcca","iccca","idcca","jccca","jdcca","kccca","kdcca","lccca","ldcca","mccca","mdcca","nccca","ndcca","occca","odcca","pccca","pdcca","ddcca","ddaca","ddada","ddbca","ddbda","ddeca","ddeda","ddfca","ddfda","ddgca","ddgda","ddhca","ddhda","ddica","ddida","ddjca","ddjda","ddkca","ddkda","ddlca","ddlda","ddmca","ddmda","ddnca","ddnda","ddoca","ddoda","ddpca","ddpda","dddda","addda","aedda","bddda","bedda","cddda","cedda","fddda","fedda","gddda","gedda","hddda","hedda","iddda","iedda","jddda","jedda","kddda","kedda","lddda","ledda","mddda","medda","nddda","nedda","oddda","oedda","pddda","pedda","eedda","eeada","eeaea","eebda","eebea","eecda","eecea","eefda","eefea","eegda","eegea","eehda","eehea","eeida","eeiea","eejda","eejea","eekda","eekea","eelda","eelea","eemda","eemea","eenda","eenea","eeoda","eeoea","eepda","eepea","eeeea","ggggg","agggg","ahggg","bgggg","bhggg","cgggg","chggg","dgggg","dhggg","egggg","ehggg","fgggg","fhggg","igggg","ihggg","jgggg","jhggg","kgggg","khggg","lgggg","lhggg","mgggg","mhggg","ngggg","nhggg","ogggg","ohggg","pgggg","phggg","hhggg","hhagg","hhahg","hhbgg","hhbhg","hhcgg","hhchg","hhdgg","hhdhg","hhegg","hhehg","hhfgg","hhfhg","hhigg","hhihg","hhjgg","hhjhg","hhkgg","hhkhg","hhlgg","hhlhg","hhmgg","hhmhg","hhngg","hhnhg","hhogg","hhohg","hhpgg","hhphg","hhhhg","ahhhg","aihhg","bhhhg","bihhg","chhhg","cihhg","dhhhg","dihhg","ehhhg","eihhg","fhhhg","fihhg","ghhhg","gihhg","jhhhg","jihhg","khhhg","kihhg","lhhhg","lihhg","mhhhg","mihhg","nhhhg","nihhg","ohhhg","oihhg","phhhg","pihhg","iihhg","iiahg","iiaig","iibhg","iibig","iichg","iicig","iidhg","iidig","iiehg","iieig","iifhg","iifig","iighg","iigig","iijhg","iijig","iikhg","iikig","iilhg","iilig","iimhg","iimig","iinhg","iinig","iiohg","iioig","iiphg","iipig","iiiig","aiiig","ajiig","biiig","bjiig","ciiig","cjiig","diiig","djiig","eiiig","ejiig","fiiig","fjiig","giiig","gjiig","hiiig","hjiig","kiiig","kjiig","liiig","ljiig","miiig","mjiig","niiig","njiig","oiiig","ojiig","piiig","pjiig","jjiig","jjaig","jjajg","jjbig","jjbjg","jjcig","jjcjg","jjdig","jjdjg","jjeig","jjejg","jjfig","jjfjg","jjgig","jjgjg","jjhig","jjhjg","jjkig","jjkjg","jjlig","jjljg","jjmig","jjmjg","jjnig","jjnjg","jjoig","jjojg","jjpig","jjpjg","jjjjg","ajjjg","akjjg","bjjjg","bkjjg","cjjjg","ckjjg","djjjg","dkjjg","ejjjg","ekjjg","fjjjg","fkjjg","gjjjg","gkjjg","hjjjg","hkjjg","ijjjg","ikjjg","ljjjg","lkjjg","mjjjg","mkjjg","njjjg","nkjjg","ojjjg","okjjg","pjjjg","pkjjg","kkjjg","kkajg","kkakg","kkbjg","kkbkg","kkcjg","kkckg","kkdjg","kkdkg","kkejg","kkekg","kkfjg","kkfkg","kkgjg","kkgkg","kkhjg","kkhkg","kkijg","kkikg","kkljg","kklkg","kkmjg","kkmkg","kknjg","kknkg","kkojg","kkokg","kkpjg","kkpkg","kkkkg","ggggx","gggxx","ggxxx","gxxxx","xxxxx","xxxxy","xxxyy","xxyyy","xyyyy","yyyyy","yyyyw","yyyww","yywww","ywwww","wwwww","wwvww","wvvww","vvvww","vvvwz","avvwz","aavwz","aaawz","aaaaz"],
            },
            output: [
                ["aaaaa","aaaaz","aaawz","aavwz","avvwz","vvvwz","vvvww","wvvww","wwvww","wwwww","ywwww","yywww","yyyww","yyyyw","yyyyy","xyyyy","xxyyy","xxxyy","xxxxy","xxxxx","gxxxx","ggxxx","gggxx","ggggx","ggggg"]
            ],
        },

    ];

    params.forEach(({ input, output }) => {
        const { beginWord, endWord, wordList } = input;
        const result = findLadders(beginWord, endWord, wordList);

        console.log(
            JSON.stringify(result) === JSON.stringify(output)
                ? "SUCCESS "
                : "ERROR ",
            "input",
            JSON.stringify(input),
            "output",
            output,
            "result",
            result,
        );
    });
};

test();
