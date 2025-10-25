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

bool isSortedasc(vector<int> &arr)
{
    for (int i = 0; i < arr.size() - 1; i++)
    {
        if (arr[i] > arr[i + 1])
            return false;
    }
    return true;
}



void solve()
{
    int t;
    cin >> t; 
    for(int d = 0; d<t; d++)
    { 
        int n; cin>>n; 
        vector<int>a(n);
        forn(0, n){
            cin>>a[i];
        }
        vector<int>b(n);
        forn(0, n){
            cin>>b[i];
        }
        bool flg = true; 
        vector<pair<int, int>>dsh;
        forn(0, n){
            if(b[i]<a[i]){
                flg = false; break; 
            }
            else{
                flg = false; 
                for(int j = 0; j<n; j++){
                    if(a[j] == b[i] && j!=i){
                        a[i]=b[i];
                        pair<int, int> x = {j, i}; 
                        dsh.pb(x); 
                        flg = true; 
                        break; 
                    }
                }
            }
        }
        if(!flg){
                cout<<"Case #"<<d+1<<": "<<-1<<endl; 
            }
        else{
            cout<<"Case #"<<d+1<<": "<<dsh.size()<<endl; 
            for(const auto &x : dsh){
                cout<<x.first<<" "<<x.second<<endl; 
            } 
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
