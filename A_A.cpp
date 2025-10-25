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
    str prv; cin>>prv; 
    int cnt=1; 
    forn(1, t){
        str x; cin>>x; 
        if(prv != x)cnt++; 
        else break; 
        prv = x; 
    }
    cout<<cnt<<endl; 
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
