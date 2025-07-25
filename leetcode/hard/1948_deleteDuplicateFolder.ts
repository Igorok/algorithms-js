function deleteDuplicateFolder(paths: string[][]): string[][] {
    class FolderNode {
        public val: string;
        public childred: Map<string, FolderNode>;
        public duplicate: boolean;

        public constructor(val: string) {
            this.val = val;
            this.childred = new Map();
            this.duplicate = false;
        }

        public get(val: string): FolderNode | undefined {
            return this.childred.get(val);
        }
        public set(val: string): void {
            const node: FolderNode = new FolderNode(val);
            this.childred.set(val, node);
        }
    }

    const root: FolderNode = new FolderNode('/');

    for (const folders of paths) {
        let node: FolderNode = root;
        for (const folder of folders) {
            const subNode: FolderNode | undefined = node.get(folder)
            if (!subNode) {
                node.set(folder);
                node = node.get(folder);
            } else {
                node = subNode;
            }
        }
    }

    const serializedTrie: Map<string, FolderNode> = new Map();
    const serialize = (node: FolderNode): string => {
        if (node.childred.size === 0) {
            return `[${node.val}]`;
        }

        const childred: string[] = [];

        const keys: string[] = [];
        node.childred.forEach((node: FolderNode) => keys.push(node.val));
        keys.sort((a, b) => a <= b ? -1 : 1);

        for (const key of keys) {
            const folder: FolderNode = node.get(key);
            const path: string = serialize(folder);
            childred.push(path);
        }

        const srtChildren: string = `[${childred.join('')}]`

        if (serializedTrie.has(srtChildren)) {
            const dupl: FolderNode = serializedTrie.get(srtChildren);
            dupl.duplicate = true;
            node.duplicate = true;
        } else {
            serializedTrie.set(srtChildren, node);
        }

        return `[${node.val}[${srtChildren}]]`
    };
    serialize(root);

    const res: string[][] = [];

    const dfs = (node: FolderNode, path: string[]) => {
        if (node.duplicate) {
            return;
        }
        path.push(node.val);
        res.push([...path]);

        node.childred.forEach((nei: FolderNode) => {
            dfs(nei, path);
        });

        path.pop();
    };

    root.childred.forEach((child: FolderNode) => {
        dfs(child, []);
    });

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                paths: [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]],
            },
            output: [["d"],["d","a"]],
        },
        {
            input: {
                paths: [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]],
            },
            output: [["c"],["c","b"],["a"],["a","b"]],
        },
        {
            input: {
                paths: [["a","b"],["c","d"],["c"],["a"]]
            },
            output: [["c"],["c","d"],["a"],["a","b"]],
        },
        {
            input: {
                paths: [["b"],["f"],["f","r"],["f","r","g"],["f","r","g","c"],["f","r","g","c","r"],["f","o"],["f","o","x"],["f","o","x","t"],["f","o","x","d"],["f","o","l"],["l"],["l","q"],["c"],["h"],["h","t"],["h","o"],["h","o","d"],["h","o","t"]],
            },
            output: [["b"],["f"],["l"],["c"],["h"],["f","r"],["f","o"],["l","q"],["h","t"],["f","r","g"],["f","o","l"],["f","r","g","c"],["f","r","g","c","r"]],
        },
    ];

    params.forEach(({ input, output }) => {
        const { paths } = input;
        const result = deleteDuplicateFolder(paths);

        console.log(
            JSON.stringify(result) === JSON.stringify(output)
                ? "SUCCESS "
                : "ERROR ",
            "input",
            JSON.stringify(input),
            "output",
            output,
            "result",
            result,
        );
    });
};

test();
