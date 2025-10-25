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
    ll t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        str s;
        cin >> s;
        int i = 0, j = n - 1;
        vector<int> ix;
        while (i < j)
        {
            if (s[i] != s[j])
            {
                ix.pb(i);
                ix.pb(j);
            }
            i++;
            j--;
        }
        if (ix.size()==0)
            cout << 0 << endl
                 << endl;
        else
        {
            bool flg = true;
            char prv = s[ix[0]];
            size_t k = 0;
            while (k < ix.size() && flg)
            {
                if (s[ix[k]] < prv)
                    flg = false;
                else
                    k++;
                prv = s[ix[k]];
            }
            if (flg)
            {
                cout << ix.size()<< endl;
                for (size_t k = 0; k < ix.size(); k++)
                {
                    cout << ix[k]+1 << " ";
                }
                cout << endl;
            }
            else
                cout << -1 << endl;
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
