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
    ll a, b, c; cin>>a>>b>>c; 
    int n; cin>>n; 
    int cnt=0; 
    forn(0,n){
        ll x; cin>>x; 
        if(x>b && x<c) cnt++; 
    }
    cout<<cnt<<endl; 
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
