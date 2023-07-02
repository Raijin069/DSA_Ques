class Solution{
    public:
    vector <int> zigZagTraversal(Node* root)
    {
    vector<int> res;
        if(root==NULL){
            return res;
        }
        int i,s,count=0;
        queue<Node*> q;
        q.push(root);
        while(!q.empty()){
            int i,s = q.size();
            vector<int> level;
            // level.push
            for(i=0;i<s;i++)
            {
                Node* node = q.front();
                q.pop();
                if(node->left != NULL){
                    q.push(node->left );
                }
                if(node->right != NULL){
                    q.push(node->right );
                }
                level.push_back(node->data);
            }
            if(count%2!=0)
            {
                reverse(level.begin(),level.end());
            }
            for (int j : level) {
                // cout << i << " ";
                res.push_back(j);
            }
            count++;
            // res.push_back(level);
        }
        return res;	// Code here
    }
};