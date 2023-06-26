#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--){
        string s;
        cin>>s;
        int ans=-1;
        map<char, int> mp;
        for(int i=0; i<s.size(); i++){
            mp[s[i]]++;;
        }
        
        for(int i=0; i<s.size(); i++){
            if(mp[s[i]]==1) {ans = i; break;}
        }
        cout<<ans;
    }

    return 0;
}
