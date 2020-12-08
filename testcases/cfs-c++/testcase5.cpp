#include<iostream>
#include<cmath>
#include<map>
#include<algorithm>
#include<vector>

int main(){
	long long m;
	std :: cin >> m;
	long long arr[m];
	long long j = 0;
	while (j < m) {
		std :: cin >> arr[j];
		j++;
	}
	std :: map<long long , long long> count;
	j = 0;
	while (j < m) {
		switch (count.find(arr[j]) == count.end()) {
			case true:
				count.insert({arr[j] , 1});
			case false:
				count[arr[j]]++;
		}
		j++;
	}
	long long alpha = 0;
	long long beta = -1;
	auto gamma = count.begin();
	while (gamma != count.end()) {
		switch (alpha <= gamma->second) {
			case true:
				alpha = gamma->second;
				beta = gamma->first;
		}
		++gamma;
	}
	std :: cout << min(2 * alpha - 1 , m) << "\n" ;
	return 0;
}
