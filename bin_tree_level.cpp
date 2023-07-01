 class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if(root==NULL){
            return res;
        }
        
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            int i,s = q.size();
            vector<int> level;
            // level.push
            for(i=0;i<s;i++)
            {
                TreeNode* node = q.front();
                q.pop();
                if(node->left != NULL){
                    q.push(node->left );
                }
                if(node->right != NULL){
                    q.push(node->right );
                }
                level.push_back(node->val);
            }
            res.push_back(level);
        }
        return res;
    }
};