
function removeSubfolders(folder: string[]): string[] {
    class Folder {
        private val: string;
        private children: Map<string, Folder>;

        public constructor(char: string) {
            this.val = char;
            this.children = new Map();
        }

        public has(char: string): boolean {
            return this.children.has(char);
        }
        public set(char: string): void {
            const folder: Folder = new Folder(char)
            this.children.set(char, folder);
        }
        public get(char: string): Folder {
            return this.children.get(char);
        }
    }

    const fileSystem: Folder = new Folder('');

    const isSubFolder = (path: string) => {
        const arr: string[] = path.split('/');

        let folder: Folder = fileSystem;
        let id: number = 0;

        while (id < arr.length) {
            if (folder.has('END')) {
                return true;
            }
            if (!folder.has(arr[id])) {
                folder.set(arr[id]);
            }
            folder = folder.get(arr[id]);
            id += 1;
        }
        folder.set('END');

        return false;
    }


    return folder
        .sort((a, b) => a.length - b.length)
        .filter((f) => !isSubFolder(f));
};

const test = () => {
    const params = [
        {
            input: {
                folder: ["/a","/a/b","/c/d","/c/d/e","/c/f"]
            },
            output: ["/a","/c/d","/c/f"],
        },
        {
            input: {
                folder: ["/a","/a/b/c","/a/b/d"]
            },
            output: ["/a"],
        },
        {
            input: {
                folder: ["/a/b/c","/a/b/ca","/a/b/d"]
            },
            output: ["/a/b/c","/a/b/ca","/a/b/d"],
        },
    ];

    params.forEach(({ input, output }) => {
        const { folder } = input;
        const result = removeSubfolders(folder);

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
