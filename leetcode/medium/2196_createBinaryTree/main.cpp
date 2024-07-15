#include<iostream>
#include<vector>
#include<map>

using std::vector;
using std::map;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        if (!descriptions.size()) return nullptr;

        map<int, TreeNode*> tree;
        map<int, int> parents;



        for (int i = 0; i < descriptions.size(); ++i) {
            int p = descriptions[i][0];
            int v = descriptions[i][1];

            TreeNode* parent;
            TreeNode* node;

            if (auto search = tree.find(p); search != tree.end()) {
                parent = tree[p];
            } else {
                parent = new TreeNode(p);
                tree[p] = parent;

                if (auto search = parents.find(p); search == parents.end()) {
                    parents[p] = -1;
                }
            }

            if (auto search = tree.find(v); search != tree.end()) {
                node = tree[v];
            } else {
                node = new TreeNode(v);
                tree[v] = node;
            }

            parents.erase(v);

            if (descriptions[i][2] == 1) {
                parent->left = node;
            } else {
                parent->right = node;
            }
        }

        return tree[parents.begin()->first];

        for (auto const& x : parents) {
            if (x.second == -1) {
                return tree[x.first];
            }
        }

        return nullptr;
    }

};

int main () {
    Solution* sol = new Solution();

    vector<vector<int>> data {
        vector<int>{20,15,1},
        vector<int>{50,20,1},
        vector<int>{20,17,0},
        vector<int>{80,19,1},
        vector<int>{50,80,0},
    };
    sol->createBinaryTree(data);





    return 0;

}
/*

[[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
        50
    20      80
  15  17   19



*/
