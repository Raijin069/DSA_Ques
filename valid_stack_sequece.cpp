// #include <iostream>
// #include <vector>
// #include <stack>
// using namespace std;

class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> s;
        int i,j;
    
        
        for(i=0,j=0;i<pushed.size();i++)
        {
            s.push(pushed[i]);
            while(!s.empty() && s.top()==popped[j]){
                s.pop();
                j++;
            }
        }

        return s.empty();
    }
};

// int main(){
//     return 0;
// }