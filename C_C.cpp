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
    ll t;
    cin >> t;
    while (t--)
    {
        int n; cin>>n; 
        set<int>a;
        vector<int< ain; 
        forn(0, n){
            int x ; cin>>x; 
            ain.pb(x); 
            a.insert(x); 
        }
        int sz = a.size(); 
        while(!flg && sz>0){
            int i = 0; 
            bool flg = true; 
            while(flg&&i<n){
                if(ain[i]%sz!=0)flg = false; 
                i++; 
            }
            if(!flg) sz--;
            else break;
        }
        
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
