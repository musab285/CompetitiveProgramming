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
    ll n, m, k;
    cin >> n >> m >> k;
    map<pair<int, int>, bool> hsh;
    forn(0, n)
    {
        ll a;
        cin >> a;
        if (a - k > 0)
            hsh[make_pair(a + k, a - k)] = false;
        else
        {
            hsh[make_pair(a + k, 1)] = false;
        }
    }
    vector<ll> b(m);
    forn(0, m)
    {
        cin >> b[i];
    }
    ll cnt = 0;
    for (auto &p : hsh)
    {
        bool flg = true;
        for (ll i=0 ; i<m && flg; i++)
        {
            if (p.second)
            {
                continue;
            }
            else if (b[i] > p.first.first)
            {
                continue;
            }
            else if (b[i] < p.first.second)
            {
                continue;
            }
            else
            {
                cnt++;
                p.second = true;
                flg = false;
            }
        }
    }
    cout << cnt << endl;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
