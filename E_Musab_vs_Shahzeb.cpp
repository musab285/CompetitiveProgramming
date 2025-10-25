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
    int n; cin>>n; 
    int ao, at, bo, bt, co, ct; cin>>ao>>at>>bo>>bt>>co>>ct;
    if(bo<ao && co>ao){
        cout<<"NO"<<endl; 
        return; 
    }
    if(bo>ao && co<ao){
        cout<<"NO"<<endl; 
        return; 
    }
    if(bt<at && ct>at){
        cout<<"NO"<<endl; 
        return; 
    }
    if(bt>at && ct<at){
        cout<<"NO"<<endl; 
        return; 
    }
    cout<<"YES"<<endl; 
    return; 
    
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
