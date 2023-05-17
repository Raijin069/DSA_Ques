#include <iostream>
#include <queue>
using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> mini;
        int i,n = nums.size();
        for(i=0;i<k;i++)
        {
            mini.push(nums[i]);
        }

        for(i=k;i<n;i++)
        {
            if(mini.top()<nums[i])
            {
                mini.pop();
                mini.push(nums[i]);
            }
        }
        return mini.top();
    }
};