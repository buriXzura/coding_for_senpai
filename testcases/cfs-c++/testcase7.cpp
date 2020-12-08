#include<bits/stdc++.h>
using namespace std;

int main(){
	int n;
	cin>>n;
	int a[n];
	map<int,int> freq;
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	int majelem=-1;
	int maxsize=0;
	for(int i=0;i<n;i++){
		if(freq.find(a[i])!=freq.end()){
			freq[a[i]]++;
		}
		else{
			freq.insert({a[i],1});
		}
	}
	for(auto itr=freq.begin();itr!=freq.end();++itr){
		if(maxsize<=itr->second){
			maxsize=itr->second;
			majelem=itr->first;
		}
	}
	cout<<min(2*maxsize-1,n)<<endl;
}
