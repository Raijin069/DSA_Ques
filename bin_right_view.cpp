class Solution
{
    public:
    //Function to return list containing elements of right view of binary tree.
    vector<int> rightView(Node *root)
    {
       vector<int> ans;
   if (root==NULL)
   {
       return ans;
   }
   queue<Node*> q;
   q.push(root);
   
   while(!q.empty())
   {
       int i,s = q.size();
       for(i=0;i<s;i++)
       {
           Node* temp = q.front();
           q.pop();
           if(i==s-1)
           {
               ans.push_back(temp->data);
           }
           if(temp->left!=NULL)
           {
               q.push(temp->left);
           }
           if(temp->right!=NULL)
           {
               q.push(temp->right);
           }
       }
   }
   return ans;
    }
};