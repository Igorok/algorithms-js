/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
	if (n === 0) {
		return arr;
	}

	const newArray = [];

	for (const item of arr) {
		if (!Array.isArray(item)) {
			newArray.push(item);
			continue;
		}
		const nestedArr = flat(item, n - 1);
		for (const nestedItem of nestedArr) {
			newArray.push(nestedItem);
		}
	}

	return newArray;
};



const test = () => {
	const params = [
		{
			depth: 0,
			arr: [0, 1, 2, [3, 4]],
		},
		{
			depth: 1,
			arr: [0, 1, 2, [3, 4]],
		},
		{
			depth: 2,
			arr: [0, 1, [2, [3, [4, 5]]]],
		},
		{
			depth: Infinity,
			arr: [0, 1, [2, [3, [4, 5]]]],
		},
	];

	params.forEach(({ arr, depth }) => {
		const r1 = flat(arr, depth);
		const r2 = arr.flat(depth);

		const equal = (JSON.stringify(r1) === JSON.stringify(r2));

		if (!equal) {
			console.log(
				'ERROR ',
				arr, depth,
				JSON.stringify(r1), JSON.stringify(r2),
			);
		} else {
			console.log(
				'OK ',
				arr, depth,
				JSON.stringify(r1), JSON.stringify(r2),
			);
		}
	});
}

test();