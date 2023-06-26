#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        long long int arr[n];
        for(int i=0; i<n; i++)cin>>arr[i];
        
        cout<<"Input Array:- ";
        for(int i=0; i<n; i++) cout<<arr[i]<<" ";
        int i=0;
        while(i<n){
            if(arr[i]==0){
                int j=i+1;
                while(j<n){
                    if(arr[j]!=0) {swap(arr[i], arr[j]); break;} 
                    j++;
                }
            } i++;
        }
        cout<<endl<<"Modified array:- ";
        for(int i=0; i<n; i++) cout<<arr[i]<<" ";
        cout<<endl;
    }

    return 0;
}
