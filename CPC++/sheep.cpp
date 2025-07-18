#include <bits/stdc++.h>
#include <algorithm>
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

void solve()
{
    ll t;
    cin >> t;
    while (t--)
    {
        ll n; 
        cin >> n;
        vector<ll> arr(n);
        ll mx = bohotchota;
        ll mn = bohotbara;
        forn(0, n){
            cin>>arr[i];
            mx = max(arr[i], mx);
            mn = min(arr[i], mn);
        }
        cout<<mx-mn<<endl; 
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
