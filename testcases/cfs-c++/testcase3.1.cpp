#include<bits/stdc++.h>
using namespace std;

void function(int aaaa, int bbbb, int cccc){
	int dddd=aaaa;
	aaaa=bbbb;
	bbbb=cccc;
	cccc=dddd;
}

void func(int xxxx, int yyyy, int zzzz){
	int qqqq=zzzz;
	zzzz=yyyy;
	yyyy=xxxx;
	xxxx=qqqq;
}

int main(){
	int n;
	cin>>n;
	int a[n];
	int i=0;
	func(1,2,3);
	while(i<n){
		cin>>a[i];
		i++;
	}
	function(1,2,3);
	map<int,int> freq;
	i=0;
	func(4,5,6);
	while(i<n){
		switch(freq.find(a[i])==freq.end()){
			case true:
				freq.insert({a[i],1});
			case false:
				freq[a[i]]++;
		}
		i++;
	}
	function(4,5,6);
	int maxsize=0;
	int majelem=-1;
	auto itr=freq.begin();
	func(7,8,9);
	while(itr!=freq.end()){
		switch(maxsize<=itr->second){
			case true:
				maxsize=itr->second;
				majelem=itr->first;
		}
		++itr;
	}
	function(7,8,9);
	cout<<min(2*maxsize-1,n)<<endl;
}
