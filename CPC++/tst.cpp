#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define forn(a, b) for (int i = a; i < b; i++)
#define forr(a, b) for (int i = a; i >= b; i--)
#define yn(x) (x ? "YES" : "NO")
#define pb push_back
#define pop pop_back
#define bohotbara INT_MAX
#define bohotchota INT_MIN

void solve()
{
    string s = "car";
    string t = "rat";
    if (s.size() != t.size()){
        cout << false;
        return;}
    sort(s.begin(), s.end());
    sort(t.begin(), t.end());
    int i = 0;
    bool flg = false;
    while (s[i] == t[i] && !flg)
    {
        if (i == s.size())
            flg = true;
        else
            i++;
    }
    cout << flg;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
