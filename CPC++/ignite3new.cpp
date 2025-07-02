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
    ll n, q;
    cin >> n;
    map<string, int> frq;
    forn(0, n)
    {
        string a;
        cin >> a;
        string pfx = "";
        for (char i : a)
        {
            pfx += i;
            sort(pfx.begin(), pfx.end());
            frq[pfx]++;
        }
    }
    cin >> q;
    forn(0, q)
    {
        string a;
        cin >> a;
        sort(a.begin(), a.end());
        if (frq[a] == 0)
        {
            cout << -1 << endl;
        }
        else
        {
            cout << frq[a] << endl;
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
