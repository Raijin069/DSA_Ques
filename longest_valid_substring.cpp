#include <iostream>
#include <string>
#include <stack>
using namespace std;

int count(string s)
{
    int count = 0;
    stack<char> st;
    for(char i:s)
    {
        if (i=='(')
        {
            st.push(i);
        }
        else if(!st.empty() && st.top()=='(')
        {
            count++;
            st.pop();
        }
        else
        {
            continue;
        }
    }
    return count*2;
}

int main(){
    string s = ""; 
    cout << count(s);
    return 0;
}