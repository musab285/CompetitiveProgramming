#include <bits/stdc++.h>
#include <string>
#include <cstring>
using namespace std;

#define ll long long int
#define str string
#define forn(a, b) for (int i = a; i < b; i++)
#define forr(a, b) for (int i = a; i >= b; i--)
#define yn(x) (x ? "YES" : "NO")
#define pb push_back
#define pop pop_back
#define bara INT_MAX
#define chota INT_MIN
#define bohotbara LLONG_MAX
#define bohotchota LLONG_MIN
#define all(x) x.begin(), x.end()

bool isSortedasc(vector<int> &arr)
{
    for (int i = 0; i < arr.size() - 1; i++)
    {
        if (arr[i] > arr[i + 1])
            return false;
    }
    return true;
}

void solve()
{
    int t;
    cin >> t;
    vector<int> e(t);
    vector<int> s(t);
    forn(0, t)
    {
        cin >> e[i];
    }
    forn(0, t)
    {
        cin >> s[i];
    }
    sort(all(e), greater<int>());
    sort(all(s));
    ll sm = 0;
    forn(0, t) sm += (e[i] * s[i]);
    cout << sm << endl;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
