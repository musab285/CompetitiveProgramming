#include <bits/stdc++.h>
#include <string>
#include <cstring>
using namespace std;

#define ll long long int
#define str string
#define forn(a, b) for (int k = a; k < b; k++)
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
    ll n, m; cin>>n>>m; 
    map<int, bool>chckr; 
    map<int, bool>chckc; 
    ll rw = n, cl=n; 
    // ll ttl = n*n; 
    forn(0, m){
        ll i, j; cin>>i>>j; 
        if(chckr[i]&&chckc[j]){
            goto chal;
        }
        else if(chckr[i]){
            cl--; 
        }
        else if(chckc[j]){
            rw--; 
        }
        else{
            rw--; cl--;  
        }
        chal:
        // cout<<rw<<cl<<endl; 
        chckr[i] = true; 
        chckc[j] = true;  
        // cout<<j<<" "<<chckc[j]<<endl;
        cout<<rw*cl<<" "; 
    }
    cout<<endl; 
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
