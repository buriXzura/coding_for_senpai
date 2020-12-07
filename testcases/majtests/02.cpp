using namespace std;
#include<iostream>
#include<unordered_map>
#include<vector>
#include<iterator>

int maxim(int a, int b){
	if(a>b) return a;
	else return b;
}

int subseqMaj(vector<int> &arr, int len) {

	//trying to solve the first part of the question
	//another random comment
	//sirf yahi question hoga agar hoga toh

	unordered_map<int,int>::iterator it;
	int crmax = 0;
	unordered_map<int, int> mp;

	for(int i=0; i<len; i++) mp[arr[i]]++;

	for(it = mp.begin(); it!=mp.end(); ++it) {
		if(it->second > len/2) return len;
		if(it->second > crmax) crmax = it->second;
	}

	int subseq = (crmax*2);
	return subseq-1;
}

int substrMaj(vector<int> &arr, int len) {

	unordered_map<int,int>::iterator it;

	//and now second part
	//chalo ek aur baar ye zaalim mindset ke andar

	int res = 0, i=0;
	unordered_map<int, int> mp;

	for(int j=0; j<len; j=j+1) {

		int crmax=0;
		mp[arr[j]]++;
		int crlen = j-i+1;

		for(it = mp.begin(); it!=mp.end(); ++it) {
			if(it->second > crmax) {crmax = it->second;}
			if(it->second > crlen/2) {res = maxim(res,crlen); break;}
		}

		if(crlen>(2*crmax)) {mp[arr[i]]--; i=i+1;}
	}

	return res;
}


int main (int argc, char*argv[]) {

	int n; cin >> n;
	vector<int> seq(n,0);

	for(int i=0; i<n; i=i+1) {
		int a;
		cin >> a;
		seq[i]=a;
	}

	int part2;
	int part1 = subseqMaj(seq,n);
	cout << part1 << endl;

	if(part1==n) {part2 = n;}
	else {part2 = substrMaj(seq,n);}
	cout << part2 << endl;

	return 0;
}
