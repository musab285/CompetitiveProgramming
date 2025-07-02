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
    str n, m;
    cin >> n >> m;
    ll ln = n.length();
    ll lm = m.length();
    ll cnt = 0;
    for (int i = 0; i < ln; i++)
    {
        bool flg = false;
        ll j = 0;
        ll k = i; 
        while (!flg && j < lm)
        {
            if (m[j] != n[k])
            {
                flg = true;
            }
            j++;
            k++; 
        }
        if (!flg)
        {
            cnt++;
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
