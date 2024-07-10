// helpers

const trigger = function () {
	const names = Object.getOwnPropertyNames(this);
	const symbols = Object.getOwnPropertySymbols(this);
	if (!symbols.length) {
		names.forEach((name) => {
			if (!name.startsWith('$')) {
				const symbol = Symbol.for(name);
				this[symbol] = this[name];
				delete this[name];
			}
		});
	} else {
		symbols.forEach((symbol) => {
			const name = Symbol.keyFor(symbol);
			this[name] = this[symbol];
			delete this[symbol];
		});
	}

};

const getter = function (key) {
	if (this[key]) return this[key];

	const symbol = Symbol.for(key);
	return this[symbol];
};

module.exports = { trigger, getter }

// example

const artObject = {
    $redRose: 11101,
    metroStations: ['Park Kultury', 'Delovoy Center'],
    busStops: ['B', 'c910', '379'],
    $city: 10101,
    towers: ['Oko', 'Neva'],
    $getTransports() {
        const stations = this.$getter('metroStations')
        const stops = this.$getter('busStops')
        return [...stations, ...stops]
    },
    $trigger: trigger,
    $getter: getter,
}

artObject.$trigger()

// basic tests


console.log(
	'keys', Object.keys(artObject),
	'metroStations', artObject.metroStations,
);

console.log('towers' in artObject) //-> false
console.log(artObject.$getter('towers')) //-> [ 'Oko', 'Neva' ]
console.log(artObject.$redRose) //-> 11101
console.log(artObject.$getTransports()) //-> [ 'Park Kultury', 'Delovoy Center', 'B', 'c910', '379' ]
