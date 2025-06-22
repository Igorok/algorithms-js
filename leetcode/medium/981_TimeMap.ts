class TimeMap {
    map: Map<string, any>;

    constructor() {
        this.map = new Map();
    }

    set(key: string, value: string, timestamp: number): void {
        const arr: any = this.map.get(key) || [];
        arr.push([timestamp, value]);
        this.map.set(key, arr);
    }

    get(key: string, timestamp: number): string {
        const arr: any = this.map.get(key) || [];

        let left: number = 0;
        let right: number = arr.length - 1;
        let res: string = '';

        while (left <= right) {
            const middle: number = Math.floor((left + right) / 2);

            if (arr[middle][0] === timestamp) {
                return arr[middle][1];
            } else if (arr[middle][0] > timestamp) {
                right = middle - 1;
            } else {
                res = arr[middle][1];
                left = middle + 1;
            }
        }

        return res;
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */

/*


Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]



 */

const test = () => {
    const params = [
        ["set", "get", "get", "set", "get", "get"],
        [["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]],
        [null, "bar", "bar", null, "bar2", "bar2"],
    ];

    const tm = new TimeMap();

    for (let i: number = 0; i < params[0].length; ++i) {
        if (params[0][i] === 'set') {
            const key: string = params[1][i][0];
            const value: string = params[1][i][1];
            const timestamp: number = params[1][i][2];

            tm.set(key, value, timestamp);
        } else {
            const key: string = params[1][i][0];
            const timestamp: number = params[1][i][1];
            const value: number = params[2][i];

            const result: string = tm.get(key, timestamp);

            console.log(
                result === value ? 'SUCCESS ' : 'ERROR ',
                'key', key,
                'timestamp', timestamp,
                'value', value,
                'result', result,
            );
        }
    }
};

test();

