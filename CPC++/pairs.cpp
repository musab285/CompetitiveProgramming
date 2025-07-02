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
    ll n;
    ll k;
    cin >> n >> k;
    vector<int> a(n);
    forn(0, n)
    {
        cin >> a[i];
    }
    map<int, int> hsh;
    for (int i : a)
    {
        hsh[i + k]++;
    }
    int prs = 0;
    for (int i : a)
    {
        if (hsh.find(i) != hsh.end())
        {
            prs += hsh[i];
        }
    }
    cout << prs << endl;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
