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
    ll t;
    cin >> t;
    while (t--)
    {
        ll n;
        cin >> n;
        bool on = false;
        vector<ll> a(n);
        ll ocnt = 0; 
        vector<ll>odd; 
        forn(0, n)
        {
            cin >> a[i];
            if (a[i] % 2 != 0){
                on = true;
                ocnt++; 
                odd.pb(a[i]); }
        }
        ll cnt = 0;
        if (on)
        {
            forn(0, n) cnt += a[i];
        }
        sort(odd.begin(), odd.end()); 
        forn(0, ocnt/2){
            cnt-= odd[i]; 
        }
        cout << cnt << endl;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
