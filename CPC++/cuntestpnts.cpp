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
    ll n; 
    cin>>n; 
    ll mx, mn, cnt=0; 
    cin>>mx; 
    mn = mx; 
    forn(1, n){
        ll crnt;
        cin>>crnt;
        if(crnt>mx){
            cnt++;
            mx = crnt;
        }else if(crnt<mn){
            cnt++; 
            mn = crnt;
        }
    }
    cout<<cnt<<endl;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
