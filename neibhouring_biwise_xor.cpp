static const int __ = []() { std::ios::sync_with_stdio(false); std::cin.tie(NULL); std::cout.tie(NULL); return 0; }();

class Solution {
public:
    bool doesValidArrayExist(vector<int>& derived) {
        int ans = 0;
        for(int i:derived)
        {
            ans^=i;
        }
        return ans==0;
    }
};