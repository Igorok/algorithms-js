/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
	return new Promise ((res, rej) => {
		let process = 0;
		const result = [];

		for (let i = 0; i < functions.length; ++i) {
			functions[i]()
				.then((r) => {
					process += 1;
					result[i] = r;
					if (process === functions.length) {
						res(result);
					}
				})
				.catch(rej);
		}
	});
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */

const promise = promiseAll([
	() => new Promise(res => res(42))
]);
promise.then(console.log); // [42]