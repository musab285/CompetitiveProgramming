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
    ll t;
    cin >> t;
    while (t--)
    {
        ll n;
        ll sum = 0;
        cin >> n;
        for (0, n)
        {
            ll x;
            cin >> x;
            sum += x;
        }
        double sqr = sqrt(sum);
        ll sqrInt = sqrt(sum);
        if (sqr == sqrInt)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
