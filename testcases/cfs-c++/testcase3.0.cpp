#include<bits/stdc++.h>
using namespace std;

int main(){
	int n;
	cin>>n;
	int a[n];
	int i=0;
	while(i<n){
		cin>>a[i];
		i++;
	}
	map<int,int> freq;
	i=0;
	while(i<n){
		switch(freq.find(a[i])==freq.end()){
			case true:
				freq.insert({a[i],1});
			case false:
				freq[a[i]]++;
		}
		i++;
	}
	int maxsize=0;
	int majelem=-1;
	auto itr=freq.begin();
	while(itr!=freq.end()){
		switch(maxsize<=itr->second){
			case true:
				maxsize=itr->second;
				majelem=itr->first;
		}
		++itr;
	}
	cout<<min(2*maxsize-1,n)<<endl;
}
