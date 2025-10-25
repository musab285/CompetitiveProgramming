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

void solve()
{
    map<int, bool> chck;
    vector<int> a(6);
    int ttl = 0;
    forn(0, 6)
    {
        cin >> a[i];
        ttl += a[i];
    }
    if (ttl % 2 != 0)
    {
        cout << "NO" << endl;
        return;
    }
    forn(0, 6)
    {
        for (int j = i + 1; j < 6; j++)
        {
            for (int k = j + 1; k < 6; k++)
            {
                int sm = a[i] + a[j] + a[k];
                if (chck[sm] && sm == ttl / 2)
                {
                    cout << "YES" << endl;
                    return;
                }
                chck[sm] = true;
            }
        }
    }
    cout << "NO" << endl;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
