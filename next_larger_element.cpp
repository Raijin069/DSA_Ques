#include <iostream>
#include <vector>
#include <stack>
using namespace std;

vector<long long> nextLargerElement(vector<long long> arr, int n){
       
        vector<long long> res(n, -1);
        int i;
    
        for(i=0;i<n-1;i++)
        {
            cout << " idx " << i << "\n";
            for(j=i+1;j<n;j++)
            {
                if(arr[i]<arr[j])
                {
                    res[i] = arr[j];
                    break;
                }
            }
            cout << res[i] << " ";
        }
        return res;
    }

int main(){
    vector<long long> v = {7,8,1,4};
    // output 8 -1 4 -1
    vector<long long> ans = nextLargerElement(v,4);
    int i;
    for(i=0;i<4;i++){
        cout << ans[i] << " ";
    }
    return 0;    
}