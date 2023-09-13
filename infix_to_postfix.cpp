#include <iostream>
#include <string>
#include <stack>
using namespace std;

int prec(char i)
{
    if (i=='^'){
        return 3;
    }
    else if (i=='*' || i=='/'){
        return 2;
    }
    else if (i=='+' || i=='-'){
        return 1;
    }
    else
    {
        return -1;
    }
}

string infix_to_postfix(string s)
{    
    string res;
    stack<char> st;
    for(char i:s)
    {
        if((i>='a' && i<='z') || (i>='A' && i<='Z'))
        {
            res+=i;
        }
        else if(i=='(')
        {
            st.push(i);
        }
        else if(i==')')
        {
            while(!st.empty() && st.top()!='(')
            {
                res+=st.top();
                st.pop();
            }
            if(!st.empty())
            {
                st.pop();
            }
        }
        else
        {
            while(!st.empty() && prec(st.top())>prec(i))
            {
                res+=st.top();
                st.pop();
            }
            st.push(i);
        }
    }
    while(!st.empty())
    {
        res+=st.top();
        st.pop();
    }
    return res;
}

int main(){
    string s;
    cout << "enter infix: ";
    cin >> s;
    cout << infix_to_postfix(s);
    return 0;
}