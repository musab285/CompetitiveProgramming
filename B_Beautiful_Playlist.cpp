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
    ll t;
    cin >> t;
    while (t--)
    {
        map<int, int>mp; 
        int n; cin>>n; 
        forn(0, n){
            int x; cin>>x; 
            mp[x]++; 
        }
        bool flg = true; 
        for(auto &i: mp){
            if(i.second>1){
                flg = false; break; 
            }
        }
        if(flg)
            cout<<"prekrasnyy"<<endl; 
        else
            cout<<"ne krasivo"<<endl; 

    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
