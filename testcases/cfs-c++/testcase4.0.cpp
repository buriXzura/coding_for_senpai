#include<iostream>
#include<cmath>
#include<map>
#include<algorithm>
#include<vector>

int main(){
	long long n;
	std :: cin >> n;
	long long a[n];
	for (long long i = 0 ; i < n ; i++) {
		std :: cin >> a[i];
	}
	std :: map<long long , long long> freq;
	for (long long i = 0 ; i < n ; i++) {
		if (freq.find(a[i]) == freq.end()) {
			freq.insert({a[i] , 1});
		}
		else {
			freq[a[i]]++;
		}
	}
	long long maxsize = 0;
	long long majelem = -1;
	for (auto itr = freq.begin() ; itr != freq.end() ; ++itr) {
		if (maxsize <= itr->second) {
			maxsize = itr->second;
			majelem = itr->first;
		}
	}
	std :: cout << min(2 * maxsize - 1 , n) << "\n" ;
	return 0;
}
