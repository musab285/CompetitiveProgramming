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
#define bohotbara INT_MAX
#define bohotchota INT_MIN

void solve()
{
    ll n, q;
    cin >> n;
    vector<string> a(n);
    forn(0, n)
    {
        cin >> a[i];
    }
    cin >> q;
    forn(0, q)
    {
        string s;
        cin >> s;
        ll cnt = 0;
        // sort(s.begin(), s.end());
        for (string x : a)
        {
            if (x.length() >= s.length())
            {
                unordered_map<char, int> frq2;
                unordered_map<char, int> frq;
                for (size_t j = 0; j < s.length(); j++)
                {
                    frq[s[j]]++;
                    frq2[x[j]]++;
                }
                bool flg = true;
                for (size_t j = 0; j < s.length() && flg; j++)
                {
                    if (frq[s[j]] != frq2[s[j]])
                        flg = false;
                }
                if (flg)
                {
                    cnt++;
                }
            }
            
        }
        if (cnt == 0)
        {
            cout << -1 << endl;
        }
        else
            cout << cnt << endl;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
