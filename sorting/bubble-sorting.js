import assert from 'node:assert';
import { Sorting } from './sorting.js';

class BubbleSorting extends Sorting {
    sort () {
        for (let i = this.array.length - 1; i > 0; i--) {
            for (let j = 0; j < i; j++) {
                if (this.array[j] > this.array[j + 1]) {
                    const tmp = this.array[j + 1];
                    this.array[j + 1] = this.array[j]
                    this.array[j] = tmp;
                }
            }
        }

        return this.array;
    }
}

const local = new BubbleSorting().sort();
const correct = new Sorting().array.sort((a, b) => a - b);

console.log(local, correct);

assert.deepEqual(local, correct);