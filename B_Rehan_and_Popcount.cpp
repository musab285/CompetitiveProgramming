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
    unsigned int t;
    cin >> t;
    int cnt = 0;
    while (t)
    {
        t &= (t - 1);
        cnt++;
    }
    unsigned j = 1;
    while (true)
    {
        int scnt=0;
        unsigned i=j; 
        while (i)
        {
            i &= (i - 1);
            scnt++;
            if (scnt == cnt)
            {
                cout << j;
                return;
            }
        }
        j++; 
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
