const handler = {
    get(target, name) {
        return name in target ? target[name] : 42;
    },
};

const p = new Proxy({}, handler);
p.a = 1;
console.log(
    'p.a', p.a,
    'p.b', p.b
); // 1, 42


const revocable = Proxy.revocable(
    { a: 1, b: 2 },
    {
        get(target, name) {
            return target[name] ? target[name] * 2 : 0;
        },
    },
);
const proxy = revocable.proxy;
console.log(
    'proxy.a', proxy.a,
    'proxy.b', proxy.b,
    'proxy.c', proxy.c,
);
revocable.revoke();
console.log(
    'proxy.a', proxy.a,
    'proxy.b', proxy.b,
    'proxy.c', proxy.c,
);