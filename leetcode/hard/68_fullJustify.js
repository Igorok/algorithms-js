/**
 * @param {string[]} words
 * @param {number} maxWidth
 * @return {string[]}
 */
var fullJustify = function(words, maxWidth) {
    const res = [];
    const buildString = (arr, length, left) => {
        const diff = maxWidth - length;
        if (arr.length === 1) {
            const spaceStr = new Array(diff).fill(' ').join('');
            return arr[0] + spaceStr;
        }

        if (left) {
            const diffEnd = maxWidth - length - arr.length + 1;
            const str = arr.join(' ') + new Array(diffEnd).fill(' ').join('');
            return str;
        }

        const avg = Math.floor(diff / (arr.length - 1));
        let remainder = (diff % (arr.length - 1));
        let str = '';
        for (let i = 0; i < arr.length; ++i) {
            str = str + arr[i];
            if (i === arr.length - 1) {
                break;
            }
            const spaceArr = new Array(avg).fill(' ');
            if (remainder) {
                spaceArr.push(' ');
                remainder -= 1;
            }
            str = str + spaceArr.join('');
        }

        return str;
    };

    let str = [];
    let chars = 0;
    for (let i = 0; i < words.length; ++i) {
        const word = words[i];
        let length = word.length;

        if (str.length > 0) {
            length += str.length;
        }

        if (chars + length > maxWidth) {
            res.push(buildString(str, chars, false));
            str = [];
            chars = 0;
        }
        str.push(word);
        chars += word.length;
    }

    if (str.length) {
        res.push(buildString(str, chars, true));
    }

    return res;
};


/*

16 - length
8 - chars
3 - words
diff = 16 - 8 = 8
space = 8 / (3 - 1) = 4


ERROR  input
[["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],20] output

[
"Science  is  what we",
"understand      well",
"enough to explain to",
"a  computer.  Art is",
"everything  else  we",
"do                  "
]

result
[
"Science  is what we",
"understand      well",
"enough to explain to",
"a  computer. Art is",
"everything  else  we",
"do                  "
]










*/

const test = () => {
    const params = [
        {
            input: [ ["This", "is", "an", "example", "of", "text", "justification."], 16],
            output: [
                "This    is    an",
                "example  of text",
                "justification.  "
             ],
        },
        {
            input: [["What","must","be","acknowledgment","shall","be"], 16],
            output: [
                "What   must   be",
                "acknowledgment  ",
                "shall be        "
              ],
        },
        {
            input: [["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20],
            output: [
                "Science  is  what we",
                "understand      well",
                "enough to explain to",
                "a  computer.  Art is",
                "everything  else  we",
                "do                  "
              ],
        },
    ];

    params.forEach(({input, output}) => {
        const result = fullJustify(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();