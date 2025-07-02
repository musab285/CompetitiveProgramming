#include <bits/stdc++.h>
using namespace std;

#define ll long long int
// #define for(a, b) for (int i = a; i < b; i++)
// #define forr(a, b) for (int i = a; i >= b; i--)
#define yn(x) (x ? "YES" : "NO")
#define pb push_back
#define pop pop_back
#define bohotbara INT_MAX
#define bohotchota INT_MIN

int containsDuplicate(vector<int>& nums) {
        set<int> hash; 
        for(int i = 0; i<nums.size(); i++){
            hash.insert(nums[i]); 
        }
        if(hash.size()<nums.size()) return hash.size(); 
        return hash.size(); 
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    vector<int> a = {1,2,3,1};
    cout<< containsDuplicate(a);
}
