import assert from 'node:assert';
import { Sorting } from './sorting.js';

class SelectionSorting extends Sorting {
    sort () {
        for (let i = 0; i < this.array.length; i++) {
            let min = i;
            for (let j = i + 1; j < this.array.length; j++ ) {
                if (this.array[j] < this.array[min]) {
                    min = j;
                }
            }
            if (min !== i) {
                const tmp = this.array[i];
                this.array[i] = this.array[min];
                this.array[min] = tmp;
            }
        }

        return this.array;
    }
}

const local = new SelectionSorting().sort();
const correct = new Sorting().array.sort((a, b) => a - b);

console.log(local, correct);
assert.deepEqual(local, correct);