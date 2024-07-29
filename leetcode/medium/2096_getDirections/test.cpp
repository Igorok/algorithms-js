class Solution {
private:

    TreeNode* getCommonParent (TreeNode* root, int startValue, int destValue) {

        if (root->val == startValue || root->val == destValue) return root;

        TreeNode* leftRoot = nullptr;
        TreeNode* rightRoot = nullptr;
        if (root->left)
            leftRoot = this->getCommonParent(root->left, startValue, destValue);

        if (root->right)
            rightRoot = this->getCommonParent(root->right, startValue, destValue);

        if (leftRoot && rightRoot) {
            return root;
        } else if (leftRoot) {
            return leftRoot;
        } else {
            return rightRoot;
        }
    }

    bool getPath (TreeNode* root, int query, string &path) {
        if (root->val == query) return true;

        if (root->left) {
            bool result = this->getPath(root->left, query, path);
            if (result) {
                path.push_back('L');
                return result;
            }
        }

        if (root->right) {
            bool result = this->getPath(root->right, query, path);
            if (result) {
                path.push_back('R');
                return result;
            }
        }

        return false;
    }

public:
    string getDirections(TreeNode* root, int startValue, int destValue) {
        if (!root) return "";

        TreeNode* parent = this->getCommonParent(root, startValue, destValue);

        string startPath = "";
        string endPath = "";

        this->getPath(parent, startValue, startPath);

        this->getPath(parent, destValue, endPath);

        startPath = startPath.size() > 0
            ? string(startPath.size(), 'U')
            : startPath;

        if (endPath.size() > 0)
            reverse(endPath.begin(), endPath.end());

        return startPath + endPath;
    }
};
