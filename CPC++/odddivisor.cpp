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
        cin >> n;
        ll i = 1;
        bool flg = false;
        while (!flg && i < sqrt(n) + 1)
        {
            if (n % i == 0)
            {
                if ((i != 1 && i % 2 == 1) || ((n / i) != 1 && (n / i) % 2) == 1)
                {
                    flg = true;
                }
            }
            i++;
        }
        if (flg)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
