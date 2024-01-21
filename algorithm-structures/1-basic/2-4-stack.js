/*
Стек с поддержкой максимума

Стек с поддержкой максимума
Реализовать стек с поддержкой операций push, pop и max.
Вход. Последовательность запросов push, pop и max .
Выход. Для каждого запроса max вывести максимальное число, находящееся на стеке.

Стек — абстрактная структура данных, поддерживающая операции push и pop.
Несложно реализовать стек так, чтобы обе эти операции работали за константное время. В данной задаче ваша цель — расширить интерфейс стека так, чтобы он дополнительно поддерживал операцию max и при этом чтобы время работы всех операций по-прежнему было константным.

Формат входа. Первая строка содержит число запросов q. Каждая из последующих q строк задаёт запрос в одном из следующих форматов: push v, pop, or max.
Формат выхода. Для каждого запроса max выведите (в отдельной строке) текущий максимум на стеке.
Ограничения. 1 <= q <= 400 000, 0 <= v <= 100 000.

Вход:
3
push 1
push 7
pop

Выход:
Выход пуст, потому что нет max запросов.

Sample Input 1:
5
push 2
push 1
max
pop
max

Sample Output 1:
2
2

Sample Input 2:
5
push 1
push 2
max
pop
max

Sample Output 2:
2
1

Sample Input 3:
10
push 2
push 3
push 9
push 7
push 2
max
max
max
pop
max

Sample Output 3:
9
9
9
9
*/




const readline = require('readline');
const assert = require('node:assert');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false,
});

let strI = 0;
let commandsSize = 0;
const commands = [];

rl.on('line', (line) => {
    if (strI === 0) {
        commandsSize = Number(line);
    } else {
        let [ command, value ] = line.split(' ');
        if (value) {
            value = Number(value);
        }
        commands.push([ command, value ]);
    }
    if (strI === commandsSize) {
        const maxResponse = getMax(commandsSize, commands);
        for (const value of maxResponse) {
            console.log(value);
        }
    }
    strI += 1;
});
rl.once('close', () => {
});

const getMax = (size, commands) => {
    // console.log(JSON.stringify({ size, commands }));
    const maxResponse = []
    if (!size) {
        return maxResponse;
    }

    const stack = [];
    const maxStack = [];
    const getMax = () => maxStack?.length ? maxStack[maxStack.length - 1] : 0;

    for (const [command, value] of commands) {
        if (command === 'push') {
            stack.push(value);
            const max = getMax();
            maxStack.push(value > max ? value : max);
            continue;
        }

        if (command === 'pop') {
            stack.pop();
            maxStack.pop();
        }

        if (command === 'max') {
            maxResponse.push(getMax());
        }
    }

    return maxResponse;
};



const test = () => {
    assert.deepEqual(getMax(3, [['push', 1],['push', 7],['pop'],]), []);
    assert.deepEqual(getMax(5, [['push',2],['push',1],['max',null],['pop',null],['max',null]]), [2,2]);
    assert.deepEqual(getMax(5, [['push',1],['push',2],['max',null],['pop',null],['max',null]]), [2, 1]);
    assert.deepEqual(getMax(10, [['push',2],['push',3],['push',9],['push',7],['push',2],['max',null],['max',null],['max',null],['pop',null],['max',null]]), [9,9,9,9,]);
    assert.deepEqual(getMax(4, [["push",5],["pop",null],["push",3],["max",null]]), [3]);
};
test();
