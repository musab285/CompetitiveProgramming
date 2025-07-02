#include <bits/stdc++.h>
using namespace std;

vector<string> sortbyfrq(vector<string> &strs)
{
    vector<string> ans;
    map<char, int> chck;
    for (string s : strs)
    {
        for (char x : s)
        {
            chck[x]++;
        }
    }

    for (const auto &p : chck)
    {
        for (string s : strs)
        {
            if (s[0] == p.first)
            {
                ans.push_back(s);
            }
        }
    }
    return ans;
}

int main()
{
    vector<string> a = {"babar", "ali", "bilal", "areeba", "hamza", "anas"};
    vector<string> ans = sortbyfrq(a);
    for (string s : ans)
    {
        cout << s << " ";
    }
}