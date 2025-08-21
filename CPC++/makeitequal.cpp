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
    int t;
    cin >> t;
    while (t--)
    {
        ll n, k;
        cin >> n >> k;
        ll s, t; 
        map<ll, ll>hshs;
        map<ll, ll>hsht; 
        forn(0, n)
        {
            cin >> s;
            hshs[s+k]++; 
            hshs[abs(s-k)]++; 
        }
        forn(0, n)
        {
            cin >> t;
            hsht[t]++; 
        }
        auto ptr = hsht.begin();
        bool flg = true; 
        while(ptr != hsht.end() && flg){
            if(ptr->second > hshs[ptr->first]){
                flg = false; 
            }
            ++ptr; 
        }
        cout<<yn(flg)<<endl ; 
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
