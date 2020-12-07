#include<bits/stdc++.h>
using namespace std;

int main(){
	int m;
	cin>>m;
	int arr[m];
	int qwert=100;
	long long yuiop=1234567890;
	for(int j=0;j<m;j++){
		cin>>arr[j];
	}
	map<int,int> count;
	char asdfg='c';
	string hjkl="qwertyuiop asdfghjkl zxcvbnm";
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
	float zxcv=12345.09876;
	boolean yes=true;
	double bnm=1234567890.0987654321;
	for(auto gamma=count.begin();gamma!=count.end();++gamma){
		if(alpha<=gamma->second){
			alpha=gamma->second;
			beta=gamma->first;
		}
	}
	cout<<min(2*alpha-1,m)<<endl;
}
