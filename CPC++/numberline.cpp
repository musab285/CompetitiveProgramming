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
    int x1, x2, v1, v2;
    cin >> x1 >> v1 >> x2 >> v2;
    int diddy = x2 - x1;
    if (v1 > v2)
    {
        int vdiddy = v1 - v2;
        cout << yn(diddy % vdiddy == 0) << endl;
    }
    else
    {
        cout << yn(0) << endl;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
