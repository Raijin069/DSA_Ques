class Solution {
public:
    
     
    vector<vector<int>> findPrimePairs(int n) {
     
        vector<vector<int>> ans;
        if(n<=3) return ans;
        if (isPrime(n-2)){
            ans.push_back({2,n-2});
        }
        int x=3;
        while(x<=(n/2))
        {
            if(isPrime(x))
            {
                if(isPrime(n-x))
                ans.push_back({x,n-x});
            }
            x+=2;
        }
        return ans;
        
    }
    
     bool isPrime(int val)
      {
          if (val==2){
              return true;
          }
          if(val%2==0){
              return false;
          }
          int x=3;
          int y=sqrt(val);
          while(x<=y)
          {
              if(val%x==0) return false;
              x+=2;
          }
          return true;
      }
};