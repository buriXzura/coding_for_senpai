//references:
//https://www.geeksforgeeks.org/check-array-majority-element/

#include<iostream>
#include<unordered_map>
#include<iterator>
#include<vector>
using namespace std;

typedef vector<int> vi;

int maxim(int a, int b){
	if(a>b) return a;
	return b;
}

bool hasMaj(unordered_map<int,int> &freqs, int len) {
	unordered_map<int,int>::iterator it;
	for(it = freqs.begin(); it!= freqs.end(); ++it){
		if(it->second > len/2) return true;
	}
	return false;
}

int subseqMaj(vi &arr, int len) {

	unordered_map<int, int> mp;
	for(int i=0; i<len; i++) mp[arr[i]]++;

	unordered_map<int,int>::iterator it;
	int crmax = 0;

	for(it = mp.begin(); it!=mp.end(); ++it) {
		if(it->second > len/2) return len;
		if(it->second > crmax) crmax = it->second;
	}

	int subseq = (crmax*2)-1;
	return subseq;
}

int substrMaj(vi &arr, int len) {

	int res = 0;
	unordered_map<int, int> mp;
	unordered_map<int,int>::iterator it;
	int i=0;

	for(int j=0; j<len; j++) {
		mp[arr[j]]++;
		int crlen = j-i+1;

		int crmax=0;
		for(it = mp.begin(); it!=mp.end(); ++it) {
			if(it->second > crmax) {crmax = it->second;}
			if(it->second > crlen/2) {res = maxim(res,crlen); break;}
		}

		if(crlen>(2*crmax)) {mp[arr[i]]--; i++;}
	}

	return res;
}


int main (int argc, char*argv[]) {

	int n; cin >> n;
	vi seq(n,0);

	for(int i=0; i<n; i++) {int a; cin >> a; seq[i]=a;}

	int part1 = subseqMaj(seq,n);
	cout << part1 << "\n";

	int part2;
	if(part1==n) {part2 = n;}
	else {part2 = substrMaj(seq,n);}
	cout << part2 << "\n";

	return 0;
}
