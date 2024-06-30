/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
	let timer;

    return (...args) => {
		if (timer) {
			clearInterval(timer);
		}
		timer = setTimeout(() => {
			timer = undefined;
			return fn(...args);
		}, t);
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */

const t = setTimeout(() => console.log(1), 5 * 1000);
console.log('t', t);