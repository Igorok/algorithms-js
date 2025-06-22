function accountsMerge(accounts: string[][]): string[][] {
    const parents: Map<string, string> = new Map();
    const count: Map<string, number> = new Map();

    const getParent = (email: string): string => {
        const parent: string | undefined = parents.get(email);
        if (!parent) {
            parents.set(email, email);
            count.set(email, 1);
            return email;
        }
        if (email === parent) {
            return email;
        }

        const grandparent: string = getParent(parent);
        parents.set(email, grandparent);

        return grandparent;
    };

    const setParent = (email1: string, email2: string) => {
        const parent1: string = getParent(email1);
        const parent2: string = getParent(email2);
        const count1: number = count.get(email1) || 0;
        const count2: number = count.get(email2) || 0;

        if (count1 < count2) {
            parents.set(parent1, parent2);
            count.set(parent2, count1 + count2);
        } else {
            parents.set(parent2, parent1);
            count.set(parent1, count1 + count2);
        }
    };

    for (const account of accounts) {
        for (let i: number = 1; i < account.length; ++i) {
            setParent(account[1], account[i]);
        }
    }

    type Group = {
        n: string, g: Set<string>,
    }
    const groups: Map<string, Group> = new Map();

    for (const account of accounts) {
        const parent: string = getParent(account[1]);
        const group: Group = groups.get(parent) || {
            n: account[0],
            g: new Set(),
        };

        for (let i: number = 1; i < account.length; ++i) {
            group.g.add(account[i]);
        }

        groups.set(parent, group);
    }

    const res: string[][] = [];

    groups.forEach((group: Group) => {
        const emails: string[] = [...group.g];
        emails.sort();

        res.push([
            group.n,
            ...emails
        ]);
    });

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                accounts: [
                    ["John","johnsmith@mail.com","john_newyork@mail.com"],
                    ["John","johnsmith@mail.com","john00@mail.com"],
                    ["Mary","mary@mail.com"],
                    ["John","johnnybravo@mail.com"]
                ],
            },
            output: [
                ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
                ["Mary","mary@mail.com"],
                ["John","johnnybravo@mail.com"]],
        },
        {
            input: {
                accounts: [
                    ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
                    ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
                    ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
                    ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
                    ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]
                ],
            },
            output: [
                ["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
                ["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
                ["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
                ["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
                ["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]
            ],
        },
    ];

    params.forEach(({input, output}) => {
        const { accounts } = input;
        const result = accountsMerge(accounts);

        const success: boolean = JSON.stringify(result) === JSON.stringify(output);
        const msg: string = success ? 'SUCCESS' : 'ERROR';
        const data = success
            ? { msg }
            : {
                msg,
                input: JSON.stringify(input),
                output,
                result,
            };

        console.log(data);
    });
};

test();

