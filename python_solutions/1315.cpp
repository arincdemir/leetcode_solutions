/*
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
*/
class Solution {
public:
    int sumO(TreeNode* root, TreeNode* grandParent, TreeNode* parent) {
        if (root == nullptr) {
            return 0;
        }
        int thisVal = 0;
        if (grandParent != nullptr && grandParent->val % 2 == 0) {
            thisVal = root->val;
        }
        return thisVal + sumO(root->left, parent, root) + sumO(root->right, parent, root);
    }

    int sumEvenGrandparent(TreeNode* root) {
        return sumO(root, nullptr, nullptr);
    }
};