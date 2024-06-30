/*

Example 1:

Input: obj = [null, 0, false, 1]
Output: [1]
Explanation: All falsy values have been removed from the array.
Example 2:

Input: obj = {"a": null, "b": [false, 1]}
Output: {"b": [1]}
Explanation: obj["a"] and obj["b"][0] had falsy values and were removed.
Example 3:

Input: obj = [null, 0, 5, [0], [false, 16]]
Output: [5, [], [16]]
Explanation: obj[0], obj[1], obj[3][0], and obj[4][0] were falsy and removed.


*/

const test = () => {
	const params = [
		{
			input: [null, 0, false, 1],
			output: [1],
		},
		{
			input: {"a": null, "b": [false, 1]},
			output: {"b": [1]},
		},
		{
			input: [null, 0, 5, [0], [false, 16]],
			output: [5, [], [16]],
		},
	];

	params.forEach(({ input, output }) => {
		const result = compactObject(input);
		if (JSON.stringify(output) === JSON.stringify(result)) {
			console.log('SUCCESS: ');
		} else {
			console.log('ERROR: ');
		}
		console.log(
			'input', input,
			'output', output,
			'result', result,
		);
	});
};


/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
	if (Array.isArray(obj)) {
		const newArray = [];
		obj.forEach((val) => {
			if (val) {
				newArray.push(compactObject(val));
			}
		});
		return newArray;
	}

	if (typeof obj === 'object') {
		const newObj = {};
		for (const k in obj) {
			if (obj[k]) {
				newObj[k] = compactObject(obj[k]);
			}
		}
		return newObj;
	}

	return obj;
};

test();

