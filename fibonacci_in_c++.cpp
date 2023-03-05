#include <iostream>
// #include<vector>
using namespace std;

// long long fib(int n,vector<long long> dp)
//     {
//         if(n==0||n==1)
//         {
//             return n;
//         }
//         else if (dp[n]!=-1)
//         {
//             /* code */
//         }
        
//     }

/*
without using dp
*/

// long long fib(int n)
//     {
//         if(n==0||n==1)
//         {
//             return n;
//         }
//         return fib(n-1) + fib(n-2);
//     }


/*
using dp 
*/

long long fib(int n,long long dp[])
    {
        if(n==0||n==1)
        {
            return n;
        }
        else if (dp[n]!=-1)
        {
            return dp[n];
        }
        else
        {
            dp[n] = fib(n-1,dp) + fib(n-2,dp);
            return dp[n];
        }
    }



int main()
    {
    cout<<"chal raha hai\n";
    int n = 50;
    long long dp[n+1];
    for(int i = 0;i<(n+1);i++)
    {
        dp[i] = -1;
    }
    cout << fib(n,dp) << "\n";
    // cout << fib(n);
    return 0;
    }