/*


8 3 10 1 6 14 4 7 13

*/

#include<iostream>
#include<queue>


struct Node {
    int value;
    Node* left;
    Node* right;
    Node* parent;

    Node(int v = -1, Node* l = NULL, Node* r = NULL, Node* p = NULL): value(v), left(l), right(r), parent(p) {}
};

struct BinaryTree
{
    Node* root = NULL;
    int size = 0;


    Node* find (int value)
    {
        if (size == 0) {
            return NULL;
        }
        Node* current = root;
        while (current->value != value) {
            if (current->value > value) {
                current = current->left;
            } else {
                current = current->right;
            }

            if (current == NULL) {
                return NULL;
            }
        }

        return current;
    }


    void insert (int value)
    {
        if (size == 0) {
            size = 1;
            Node *node = new Node(value, NULL, NULL, NULL);
            root = node;
            return;
        }

        Node* current = root;

        while (current->value != value) {
            if (current->value > value) {
                if (current->left == NULL) {
                    size += 1;
                    current->left = new Node(value, NULL, NULL, current);
                }
                current = current->left;
            } else {
                if (current->right == NULL) {
                    size += 1;
                    current->right = new Node(value, NULL, NULL, current);
                }
                current = current->right;
            }

        }
    }

    /*
    * successor - next largest value
    * 1) If node has right child, looking for last left child of right child
    * 2) If node has node right child. Looking for node which is left node of his parent. This parent is next largest value.
    */
    Node* successor(Node* node)
    {
        if (node->right != NULL) {
            Node* current = node->right;
            while (current->left != NULL) {
                current = current->left;
            }
            return current;
        } else {
            Node* current = node->parent;
            while (current->parent != NULL) {
                if (current == current->parent->left) {
                    return current->parent;
                }
                current = current->parent;
            }
        }

        return NULL;
    }


    void print()
    {
        std::queue<Node*> q;
        q.push(root);
        std::cout << root->value << "\n";

        while (!q.empty()) {
            Node *node = q.front();
            q.pop();

            if (node->left != NULL) {
                q.push(node->left);
                std::cout << node->left->value << "(" << node->value << ")" << "    ";
            }
            if (node->right != NULL) {
                q.push(node->right);
                std::cout << node->right->value << "(" << node->value << ")" << "    ";
            }
            std::cout << "\n";
        }

    }

};





int main()
{
    int length;
    std::cin >> length;

    BinaryTree bTree;
    for (int i = 0; i < length; ++i) {
        int value;
        std::cin >> value;
        bTree.insert(value);
    }

    bTree.print();

    Node* n1 = bTree.find(8);
    std::cout << "n1 " << n1->value << "\n";

    Node* s1 = bTree.successor(n1);
    std::cout << "s1 " << s1->value << "\n";

    Node* n2 = bTree.find(6);
    std::cout << "n2 " << n2->value << "\n";

    Node* s2 = bTree.successor(n2);
    std::cout << "s2 " << s2->value << "\n";

    return 0;
}
