


class EventEmitter {
	events = new Map();
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {
		if (!this.events.has(eventName)) {
			this.events.set(eventName, new Map())
		}
		const cb = Math.random() * 1000 + callback.toString();
		const callbacks = this.events.get(eventName);
		callbacks.set(cb, callback);

        return {
            unsubscribe: () => {
				callbacks.delete(cb);
            }
        };
    }

    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
		if (!this.events.has(eventName)) {
			return [];
		}
		const results = [];
		const callbacks = this.events.get(eventName);
		callbacks.forEach((cb) => {
			const r = cb(...args);
			results.push(r);
		});

		return results;
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */