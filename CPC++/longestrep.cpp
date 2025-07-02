#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define for(a, b) for (int i = a; i < b; i++)
#define forr(a, b) for (int i = a; i >= b; i--)
#define yn(x) (x ? "YES" : "NO")
#define pb push_back
#define pop pop_back
#define bohotbara INT_MAX
#define bohotchota INT_MIN

void solve()
{
    string s;
    cin >> s;
    int mxcnt = 1;
    char prv = s[0];
    int cnt = 1;
    for (1, s.size())
    {
        if (prv == s[i])
        {
            cnt++;
        }
        else
        {
            prv = s[i];
            // cout << s[i];
            cnt = 1;
        }
        mxcnt = max(cnt, mxcnt);
    }
    cout << mxcnt << endl;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
