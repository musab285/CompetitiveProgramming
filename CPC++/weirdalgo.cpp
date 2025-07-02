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
    ll t;
    cin >> t;
    cout << t << " ";
    while (t != 1)
    {

        if (t % 2 == 0)
        {
            t /= 2;
        }
        else
        {
            t = (t * 3) + 1;
        }
        cout << t << " ";
    }
    cout << endl;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
