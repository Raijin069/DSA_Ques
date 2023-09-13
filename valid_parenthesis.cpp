class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        unordered_map<char, char> umap;
        umap['['] = ']';
        umap['{'] = '}';
        umap['('] = ')';

    
    for(char i:s)
    {
        
        if(umap.count(i)){
            st.push(i);
        }
        else if(st.size()!=0 && i==umap[st.top()])
        {
            st.pop();
        }
        else
        {   
            return false;
        }
    }
        return st.size() == 0;  
    }
};