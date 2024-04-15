
class Node {
    constructor({ key = 0, height = 1, left, right }) {
        this.key = key;
        this.height = height;
        this.left = left;
        this.right = right;
    }

    /**
     * @returns {number} difference between height of right and left children's
     */
    getBalanceFactor() {
        const lHeight = this.left ? this.left.height : 0;
        const rHeight = this.right ? this.right.height : 0;
        return rHeight - lHeight;
    }

    /**
     * calculate height of node, from heights of left and right children's
     */
    fixHeight() {
        const lHeight = this.left ? this.left.height : 0;
        const rHeight = this.right ? this.right.height : 0;
        this.height = (lHeight > rHeight ? lHeight : rHeight) + 1;
    }
}

class AvlTree {
    constructor() {
        this.root = undefined;
    }

    /**
     * Left rotation
     * 1) Right child became new root
     * 2) Node lose right child, and left child of old right child became new right child of the node
     * 3) Old right child lose left child, and node became new left child of the new root
     * @param {object} node
     * @returns {object}
     */
    rotateLeft(node) {
        const root = node.right;

        const left = node;
        left.right = root.left;
        root.left = left;

        left.fixHeight();
        root.fixHeight();

        return root;
    }

    /**
     * Right rotation
     * 1) Left child became new root
     * 2) Node lose left child, and right child of old left child became new left child of the node
     * 3) Old left child lose right child, and node became new right child of the new root
     * @param {object} node
     * @returns {object}
     */
    rotateRight(node) {
        const root = node.left;

        const right = node;
        right.left = root.right;
        root.right = right;

        right.fixHeight();
        root.fixHeight();

        return root;
    }

    /**
     * AVL trees have a balancing factor. This calculates the difference between height of a right subtree and height of a left subtree.
     * There are 4 cases for balancing.
     * If we have a balance factor equal 2, this means the right subtree is too long, we have to apply left rotation.
     * If we have a balance factor equal 2, and the balance factor of our right child is negative.
     * We have to apply right rotation for our right child and after left rotation for the current vertex.
     * Same procedure for left subtree.
     * If we have a balance factor equal -2, this means our left subtree is too long. We have to apply the right rotation.
     * If we have a balance factor equal -2, and the balance factor of our left child is positive.
     * We have to apply left rotation for our left child and after right rotation for the current vertex.
     * @param {object} node
     * @returns {object}
     */
    balance(node) {
        node.fixHeight();

        if (node.getBalanceFactor() === 2 ) {
            if (node.right.getBalanceFactor() < 0) {
                node.right = this.rotateRight(node.right);
            }
            return this.rotateLeft(node);
        }

        if (node.getBalanceFactor() === -2) {
            if (node.left.getBalanceFactor() > 0) {
                node.left = this.rotateLeft(node.left);
            }
            return this.rotateRight(node);
        }

        return node;
    }

    insert(node) {
        if (! this.root) {
            this.root = node;
            return;
        }
        this.root = this._insert(this.root, node);
    }

    /**
     * Insertion of new node
     * If node less that current node we need to insert in left child
     * If node value bigger that current node we need to insert in right child
     * After insertion of a new node, we should restore balance. Method of balancing works from new node to root for all subtrees by recursion.
     * @param {object} vertex - vertex of the tree
     * @param {object} node - new node
     */
    _insert(vertex, node) {
        if (node.key === vertex.key) {
            return vertex;
        }
        if (node.key < vertex.key) {
            if (! vertex.left) {
                vertex.left = node;
            } else {
                vertex.left = this._insert(vertex.left, node);
            }
        } else {
            if (! vertex.right) {
                vertex.right = node;
            } else {
                vertex.right = this._insert(vertex.right, node);
            }
        }

        return this.balance(vertex);
    }

    findMin(node) {
        return node.left ? this.findMin(node.left) : node;
    }

    /**
     * Removing a minimum in subtree.
     * If a vertex has no left child, we replace the current vertex by the right child.
     *
     * If a vertex has a left child we apply a function for the left child.
     * If a left child has a right child this will be replaced. If a left child has no children this will be replaced by undefined, removed.
     *
     * @param {object} node
     * @returns {object}
     */
    removeMin(node) {
        if (! node.left) {
            return node.right;
        }
        node.left = this.removeMin(node.left);
        return this.balance(node);
    }

    remove(k) {
        this.root = this._remove(this.root, k);
        return this.root;
    }

    /**
     * Removing a node. This is a recursive function.
     * If the current node less that value we will look in the left subtree.
     * If the current node is bigger that value we will look in the right subtree.
     *
     * There are two cases here:
     * Node has no right subtree, we have to replace the current vertex to the left child.
     *
     * Node has a right subtree. We have to find the minimum value in the right subtree, to change the current vertex.
     * After changing vertices we need to remove a minimum value from the right subtree.
     * @param {object} node - current vertex of the tree
     * @param {number} k - value for remove
     * @returns {object|undefined}
     */
    _remove(node, k) {
        if (! node) {
            return;
        }

        if (k < node.key) {
            node.left = this._remove(node.left, k);
        } else if (k > node.key) {
            node.right = this._remove(node.right, k);
        } else {
            if (! node.right) {
                return node.left;
            }

            const min = this.findMin(node.right);
            node.key = min.key;
            node.right = this.removeMin(node.right);

            node = this.balance(node);
        }

        return node;
    }

    find(k, node) {
        if (! node) {
            node = this.root;
        }

        if (k === node.key) {
            return node;
        } else if (k < node.key) {
            if (! node.left) {
                return;
            }
            return this.find(k, node.left);
        } else if (k > node.key) {
            if (! node.right) {
                return;
            }
            return this.find(k, node.right);
        }
    }
}


const printTree = (binaryTree) => {
    const layers = [];

    const queue = [
        {
            node: binaryTree.root,
            layer: 0,
        }
    ];


    while (queue.length) {
        const { node, layer, parent } = queue.shift();

        layers[layer] = layers[layer] || [];
        layers[layer].push(`${node.key}(${parent || ''})`);

        if (node.left) {
            queue.push({
                node: node.left,
                layer: layer + 1,
                parent: node.key + ':l',
            });
        }

        if (node.right) {
            queue.push({
                node: node.right,
                layer: layer + 1,
                parent: node.key + ':r'
            });
        }
    }

    for (let i = 0; i < layers.length; ++i) {
        const layer = layers[i];
        const tabs = new Array(layers.length - i).fill('    ').join('');
        const str = layer.join('    ');
        console.log(tabs + str + '\n');
    }

}

const main = () => {
    const avl = new AvlTree();

    for (let i = 1; i < 11; ++i) {
        const n = new Node({ key: i });
        avl.insert(n);
    }

    printTree(avl);

    avl.insert(new Node({key: 11}));
    printTree(avl);

    avl.remove(10);
    printTree(avl);

};

main();

