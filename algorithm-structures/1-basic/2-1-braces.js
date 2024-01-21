/*

Скобки в коде
Проверить, правильно ли расставлены скобки в данном коде.
Вход. Исходный код программы.
Выход. Проверить, верно ли расставлены скобки. Если нет, выдать индекс первой ошибки.

Вы разрабатываете текстовый редактор для программистов и хотите реализовать проверку корректности расстановки скобок. В коде могут встречаться скобки []{}(). Из них скобки [,{ и ( считаются открывающими, а соответствующими им закрывающими скобками являются ],} и ).
В случае, если скобки расставлены неправильно, редактор должен также сообщить пользователю первое место, где обнаружена ошибка. В первую очередь необходимо найти закрывающую скобку, для которой либо нет соответствующей открывающей (например, скобка ] в строке “]()”), либо же она закрывает не соответствующую ей открывающую скобку (пример: “()[}”). Если таких ошибок нет, необходимо найти первую открывающую скобку, для которой нет соответствующей закрывающей (пример: скобка ( в строке “{}([]”).
Помимо скобок, исходный код может содержать символы латинского алфавита, цифры и знаки препинания.
Формат входа. Строка s[1 . . . n], состоящая из заглавных и прописных букв латинского алфавита, цифр, знаков препинания и скобок из множества []{}().
Формат выхода. Если скобки в s расставлены правильно, выведите строку “Success". В противном случае выведите индекс (используя индексацию с единицы) первой закрывающей скобки, для которой нет соответствующей открывающей. Если такой нет, выведите индекс первой открывающей скобки, для которой нет соответствующей закрывающей.

Пример.
Вход:
[]
Выход:
Success

Пример.
Вход:
{}[]
Выход:
Success

Пример.
Вход:
[()]
Выход:
Success

Пример.
Вход:
(())
Выход:
Success

Пример.
Вход:
{[]}()
Выход:
Success

Пример.
Вход:
{
Выход:
1

Пример.
Вход:
{[}
Выход:
3

Пример.
Вход:
foo(bar);
Выход:
Success

Пример.
Вход:
foo(bar[i);
Выход:
10
*/

const readline = require('readline');
const assert = require('node:assert');


const checkBraces = (str) => {
    if (!str?.length) {
        return 'Success';
    }

    const stack = [];
    const open = {
        '(': ')',
        '[': ']',
        '{': '}',
    };
    const close = {
        ')': '(',
        ']': '[',
        '}': '{',
    };
    for (let i = 0; i < str.length; i++) {
        const char = str[i];
        if (open[char]) {
            stack.push({ char, i: i + 1 });
            continue;
        }
        if (close[char]) {
            if (!stack.length) {
                return i + 1;
            }
            const past = stack.pop();
            if (close[char] !== past.char) {
                return i + 1;
            }
        }
    }

    if (stack[0]) {
        return stack[0].i;
    }

    return 'Success'
};

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

rl.on('line', (line) => {
    const result = checkBraces(line);
    console.log(result);
});

rl.once('close', () => {
});

const test = () => {
    assert.equal(checkBraces('[]'), 'Success');
    assert.equal(checkBraces('{}[]'), 'Success');
    assert.equal(checkBraces('[()]'), 'Success');
    assert.equal(checkBraces('(())'), 'Success');
    assert.equal(checkBraces('{[]}()'), 'Success');
    assert.equal(checkBraces('{'), '1');
    assert.equal(checkBraces('{[}'), '3');
    assert.equal(checkBraces('foo(bar);'), 'Success');
    assert.equal(checkBraces('foo(bar[i);'), '10');
    assert.equal(checkBraces('(()'), '1');
    assert.equal(checkBraces('()[]}'), 5);
};
test();

