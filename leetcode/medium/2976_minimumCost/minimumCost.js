class Node {
    constructor(val, priority) {
      this.val = val;
      this.priority = priority;
    }
}

class PriorityQueue {
    constructor() {
      this.values = [];
    }
    enqueue(val, priority) {
      let newNode = new Node(val, priority);
      this.values.push(newNode);
      this.bubbleUp();
    }
    bubbleUp() {
      let idx = this.values.length - 1;
      const element = this.values[idx];
      while (idx > 0) {
        let parentIdx = Math.floor((idx - 1) / 2);
        let parent = this.values[parentIdx];
        if (element.priority >= parent.priority) break;
        this.values[parentIdx] = element;
        this.values[idx] = parent;
        idx = parentIdx;
      }
    }
    dequeue() {
      const min = this.values[0];
      const end = this.values.pop();
      if (this.values.length > 0) {
        this.values[0] = end;
        this.sinkDown();
      }
      return min;
    }
    sinkDown() {
      let idx = 0;
      const length = this.values.length;
      const element = this.values[0];
      while (true) {
        let leftChildIdx = 2 * idx + 1;
        let rightChildIdx = 2 * idx + 2;
        let leftChild, rightChild;
        let swap = null;

        if (leftChildIdx < length) {
          leftChild = this.values[leftChildIdx];
          if (leftChild.priority < element.priority) {
            swap = leftChildIdx;
          }
        }
        if (rightChildIdx < length) {
          rightChild = this.values[rightChildIdx];
          if (
            (swap === null && rightChild.priority < element.priority) ||
            (swap !== null && rightChild.priority < leftChild.priority)
          ) {
            swap = rightChildIdx;
          }
        }
        if (swap === null) break;
        this.values[idx] = this.values[swap];
        this.values[swap] = element;
        idx = swap;
      }
    }
  }


/**
 * @param {string} source
 * @param {string} target
 * @param {character[]} original
 * @param {character[]} changed
 * @param {number[]} cost
 * @return {number}
 */
var minimumCost = function(source, target, original, changed, cost) {
    const graph = new Map();
    for (let i = 0; i < original.length; ++i) {
        const from = original[i];
        const to = changed[i];
        const weight = cost[i];

        const nodes = graph.has(from) ? graph.get(from) : [];
        nodes.push([to, weight]);
        graph.set(from, nodes);
    }



    const search = (from) => {
        const path = new Map();
        path.set(from, 0);

        const dfs = (from, cost) => {
            const nodes = graph.has(from) ? graph.get(from) : [];
            for (const [nei, weight] of nodes) {
                if (!path.has(nei) || path.get(nei) > weight + cost ) {
                    path.set(nei, weight + cost);
                    dfs(nei, weight + cost);
                }
            }
        }

        dfs(from, 0);

        return path;
    };

	const allPath = new Map();
	new Set(source).forEach((from) => {
		allPath.set(from, search(from));
	});



    let result = 0;
    for (let i = 0; i < source.length; ++i) {
        if (source[i] !== target[i]) {
            const path = allPath.get(source[i]);
            if (!path.has(target[i])) return -1;
            result += path.get(target[i]);
        }
    }


    return result;
};


const test = () => {
    const params = [
        {
            input: [
                "abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]
            ],
            output: 28,
        },
        {
            input: [
                "aaaa", "bbbb", ["a","c"], ["c","b"], [1,2]
            ],
            output: 12,
        },
    ];

    params.forEach(({ input, output }) => {
        const result = minimumCost(...input);
        console.log(
            (output === result) ? 'SUCCESS' : 'ERROR',
            '\n input', input,
            '\n output', output,
            '\n result', result,
        );
    });
};

test();