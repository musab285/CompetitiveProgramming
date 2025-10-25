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
    int t;
    cin >> t;
    ll mx = bohotchota; 
    forn(0, t){
        ll x; cin>>x; 
        mx = max(mx, x); 
    }
    if(mx>25)cout<<mx-25<<endl; 
    else cout<<0<<endl; 
    
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
