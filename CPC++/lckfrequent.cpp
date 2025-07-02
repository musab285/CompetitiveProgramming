#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> nums = {3, 0, 1, 0};
    map<int, int> hsh;
    for (auto i : nums)
    {
        hsh[i]++;
    }
    for (auto &i : hsh)
    {
        cout << "KEY: " << i.first << "VALUE: " << i.second << endl;
    }
    vector<int> ans;
    int k = 1;
    // int x = 1;
    int prv = INT_MAX;
    for (int i = 0; i < k; i++)
    {
        int mx = INT_MIN;
        int mxi;
        for (const auto &p : hsh)
        {
            if (p.second <= prv && p.second > mx && p.first != mxi)
            {
                mx = p.second;
                mxi = p.first;
            }
        }
        ans.push_back(mxi);
        prv = mx;
    }
    for (auto x : ans)
    {
        cout << x << endl;
    }
}
