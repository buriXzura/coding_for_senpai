#include<bits/stdc++.h>
using namespace std;

int main(){
	int n;
	cin>>n;
	int a[n];
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	map<int,int> freq;
	for(int i=0;i<n;i++){
		if(freq.find(a[i])==freq.end()){
			freq.insert({a[i],1});
		}
		else{
			freq[a[i]]++;
		}
	}
	int maxsize=0;
	int majelem=-1;
	for(auto itr=freq.begin();itr!=freq.end();++itr){
		if(maxsize<=itr->second){
			maxsize=itr->second;
			majelem=itr->first;
		}
	}
	cout<<min(2*maxsize-1,n)<<endl;
}
