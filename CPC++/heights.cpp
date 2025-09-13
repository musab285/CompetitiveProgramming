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
    int n;
    cin >> n;
    vector<int> a(n);
    vector<int> tmp;
    forn(0, n)
    {
        cin >> a[i];
        if (i == 0)
            cout << -1 << endl;
        else
        {
            sort(tmp.begin(), tmp.end());
            int lw = 0, hg = i-1;
            int ans = -1; 
            while (lw <= hg)
            {
                int mid = (lw+hg)/2; 
                if(tmp[mid]>a[i]) hg=mid-1; 
                else{
                    ans=tmp[mid]; 
                    lw=mid+1; 
                }
            }
            if(ans==-1) cout<<-1<<endl; 
            else cout<<ans<<endl; 
        }
        tmp.pb(a[i]);
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}
