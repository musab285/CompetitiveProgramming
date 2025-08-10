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

// bool isSortedasc(vector<int> &arr)
// {
//     for (int i = 0; i < arr.size() - 1; i++)
//     {
//         if (arr[i] > arr[i + 1])
//             return false;
//     }
//     return true;
// }



void solve()
{
    ll t;
    cin >> t;
    while (t--)
    {
        ll n, k; cin>>n>>k; 
        ll sm = 0; 
        ll mn1 = bohotbara; 
        ll mn2 = bohotbara; 
        forn(0, n){
            ll x; cin>>x; 
            sm+= x; 
            if(x<mn1){
                mn2 = mn1; 
                mn1 = x; 
            }else if(x<mn2){
                mn2 = x; 
            }
        }
        // cout<<mn1<<" "<<mn2<<" "; 
        ll prv; 
        if((mn1 + mn2)%2==0) prv=(mn1+mn2)/2;
        else prv = (mn1+mn2+1)/2; 
        sm+=prv;
        if(prv<=mn1){
            mn2=mn1; 
            mn1 = prv; 
        }
        else if(prv<mn2) mn2=prv; 

        if((mn1 + mn2)%2==0) prv=(mn1+mn2)/2;
        else prv = (mn1+mn2+1)/2; 

        sm+=(prv*(k-1)); 
        
        if(t>0)cout<<sm<<endl;
        else cout<<sm; 
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
