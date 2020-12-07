#include<bits/stdc++.h>
using namespace std;

int main(){
	int m;
	cin>>m;
	int arr[m];
	for(int j=0;j<m;j++){
		cin>>arr[j];
	}
	map<int,int> count;
	for(int j=0;j<m;j++){
		if(count.find(arr[j])==count.end()){
			count.insert({arr[j],1});
		}
		else{
			count[arr[j]]++;
		}
	}
	int alpha=0;
	int beta=-1;
	for(auto gamma=count.begin();gamma!=count.end();++gamma){
		if(alpha<=gamma->second){
			alpha=gamma->second;
			beta=gamma->first;
		}
	}
	cout<<min(2*alpha-1,m)<<endl;
}
