const obj = { a: 1, b: 2 };
const proxyParam = {
    get(target, prop, receiver) {
        console.log('Get', prop);

        if (!Reflect.has(target, prop)) {
            return 0;
        }

        return Reflect.get(target, prop) * 2;
    },
    set(target, prop, value) {
        console.log('Set', prop, value);
        Reflect.set(target, prop, value);
    }
};
const proxied = new Proxy({...obj}, proxyParam);
proxied.c = 3;
console.log(
    'proxied.a', proxied.a,
    'proxied.b', proxied.b,
    'proxied.c', proxied.c,
    'proxied.d', proxied.d,
);

const revocable = Proxy.revocable({...obj}, proxyParam);
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