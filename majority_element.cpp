#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// class Solution {
// public:
//     int majorityElement(vector<int>& nums) {
//         int n=nums.size(),cnt=1,i;
//         if(n==1)
//         {
//             return nums[0];
//         }
//         sort(nums.begin(),nums.end());
//         for(i=1;i<=n;i++)
//         {
//             if(num[i-1]==nums[i])
//             {
//                 cnt++;
//             }
//             else
//             {
//                if(cnt > n/2)
//                {
//                    return arr[i-1];
//                }
//                 cnt=1;
//             }
            
//         }
//         return -1;
//     }
// };

int majorityElement(int *arr, int n)
{
    if (n == 1) return arr[0];
     
    int cnt = 1;
      // sort the array, o(nlogn)
    sort(arr, arr + n);
    for (int i = 1; i <= n; i++){
        if (arr[i - 1] == arr[i]){
            cnt++;
        }
        else{
            if (cnt > n / 2){
                return arr[i - 1];
            }
            cnt = 1;
        }
    }
    // if no majority element, return -1
    return -1;
}