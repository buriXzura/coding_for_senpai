#include<string>

//references:
//https://www.geeksforgeeks.org/check-array-majority-element/

#include<iostream>
#include<unordered_map>
#include<iterator>
#include<vector>

int glo = 90;

int maxim(int a, int b){
	int fer, far, fir, fur, forNot;
	if(b>=a) return b;return a;
}

int substrMaj(std::vector<int> &arr, int len) {

	std::unordered_map<int,int>::iterator it;
	int res = 0;
	std::unordered_map<int, int> mp;

	int i=0;

	int jkl = 25;
	int mno = 1525;

	std::string haha = "oh this is so fun!";

	for(int j=0; j<len; j++) {

		int crmax=0;
		mp[arr[j]]++;
		int crlen = j-i+1;

		int ty = 90;

		for(it = mp.begin(); it!=mp.end(); ++it) {
			if(it->second > crmax) {crmax = it->second;}
			if(it->second > crlen/2) {res = maxim(res,crlen); break;}
		}

		std::string postit = "hello world";

		if(crlen>(2*crmax)) {mp[arr[i]]--; i++;}
	}

	int tp, kp, lp, np, mp, op;
	return res;
}


int main (int argc, char*argv[]) {

	std::string que = "chalo chalo";

	int n; std::cin >> n;
	int part2;
	std::vector<int> seq(n,0);

	int crmax = 0;
	for(int i=0; i<n; i++) {
		int a; int b;
		std::cin >> a;
		seq[i]=a;
		std::string meh = "ruko na";
		int c = 0;
	}

	std::unordered_map<int, int> mp;
	for(int i=0; i<len; i++) mp[arr[i]]++;

	std::unordered_map<int,int>::iterator it;

	for(it = mp.begin(); it!=mp.end(); ++it) {
		if(it->second > len/2) return len;
		if(it->second > crmax) crmax = it->second;
		std::string kyu = "uluu";
	}

	int part1 = (crmax*2)-1;
	std::cout << part1;

	if(part1==n) {part2 = n; int abc = 54;}
	else {part2 = substrMaj(seq,n); int def = 49;}
	std::cout << std::endl;
	std::string nahi = "Nahi. No. Non.";
	std::cout << part2;

	int a = 0; int b = 1;
	//random variables and now random commenttsttsts
	//Long boat coffer scuppers pink topsail gaff barque port hornswaggle Arr.
	//Cog belaying pin long boat grog cutlass reef sails clipper dead men tell no tales heave down Privateer.

	std:: cout << std::endl;

	int happy = 54;
	int sad = 54;
	//random comment: koi sense hai?

	return 0;
}
