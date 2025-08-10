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
    ll t;
    cin >> t;
    map<ll, ll>hsh;
    while (t--)
    {
        ll mxf= bohotchota;
        // ll cnt=0;
        ll n;
        cin>>n;
        hsh.clear();
        forn(0, n){
            ll x;
            cin>>x;
            hsh[x]++; 
            if(hsh[x]>mxf){
                mxf=hsh[x];
            }
        }
        cout<<n-mxf<<endl;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
