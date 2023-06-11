#include <iostream>
#include <vector>
using namespace std;

class Solution {
    int search(vector<int> &nums,int l,int r)
    {
        if(l==r) return nums[l];
        int mid = l+(r-l)/2;
        if (nums[mid] > nums[r]) return search(nums,mid+1,r);
        if (nums[mid] < nums[r]) return search(nums,l,mid);
        return nums[r];
            
    }
public:
    int findMin(vector<int>& nums) {
        int n = nums.size();
        return search(nums,0,n-1);
    }
};

int main()
{
    Solution a;
    vector<int> nu = {1,2,3,4,5,6,7,8,9}; 
    cout << a.findMin(&nu);
    return 0;
}