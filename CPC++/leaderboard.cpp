#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define str string
#define forn(a, b) for (int i = a; i < b; i++)
#define forr(a, b) for (int i = a; i >= b; i--)
#define yn(x) (x ? "YES" : "NO")
#define pb push_back
#define pop pop_back
#define bohotbara INT_MAX
#define bohotchota INT_MIN

void solve()
{
    int n, m;
    cin >> n;
    vector<int> rnkd(n);
    vector<int> md;
    int prv = bohotchota;
    int rank = 0;
    forn(0, n)
    {
        cin >> rnkd[i];
        if (rnkd[i] != prv)
        {
            rank++;
            md.push_back(rnkd[i]);
        }
        prv = rnkd[i];
    }
    cin >> m;
    vector<int> plyr(m);
    vector<int> ans;
    forn(0, m)
    {
        cin >> plyr[i];
        size_t x = 0;
        bool flg = true;
        while (flg && x < md.size())
        {
            // if (x == md.size() - 1)
            // {
            //     ans.push_back(x + 2);
            //     flg = false;
            // }else{
            // cout << md[x] << "i:" << i << endl;
            if (plyr[i] >= md[x])
            {
                ans.push_back(x + 1);
                // cout << "ANS" << ans[i] << endl;
                flg = false;
            }
            x++;
            if (flg && x == md.size())
            {
                ans.push_back(x + 1);
                flg = false;
            }
        }
    }
    for (auto i : ans)
    {
        cout << i << endl;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
