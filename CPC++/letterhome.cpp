#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define for(a, b) for (int i = a; i < b; i++)
#define forr(a, b) for (int i = a; i >= b; i--)
#define yn(x) (x ? "YES" : "NO")
#define pb push_back
#define pop pop_back
#define bohotbara INT_MAX
#define bohotchota INT_MIN

void solve()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, s;
        cin >> n >> s;
        int cnt;
        vector<int> x(n);
        for (0, n)
        {
            cin >> x[i];
            // cout<<x[i];
        }
        // cout<<x[0]<<"x0"<<s<<endl; 
        // int flg = s>x[0]; 
        // cout<<flg<<endl;
        if (s > x[0])
        {
            cnt = (s - x[0]) + (x[n - 1]-x[0]);
        }
        else
        {
            int mn;
            // cout<<"YES"<<endl;
            if(n==1){
                mn = abs(s-x[0]);
            }
            else{
            int mn = x[1] - x[0];
            for (1, n)
            {
                mn = min(mn, x[i + 1] - x[i]);
                // cout<<"mn"<<mn<<endl;
            }}
            cnt = (2 * mn) + (x[n - 1] - s);
        }
        cout << cnt << endl;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
