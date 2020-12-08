#include<iostream>
#include<cmath>
#include<map>
#include<algorithm>
#include<vector>

int main(){
	long long n; //this is a variable
	std :: cin >> n; //this is input statement
	long long a[n]; //this is an array

	for (long long i = 0 ; i < n ; i++) { //this is a for loop
		std :: cin >> a[i]; //this is just a comment
	}

	std :: map<long long , long long> freq; //this is a map

	for (long long i = 0 ; i < n ; i++) { //another for loop?
		if (freq.find(a[i]) == freq.end()) { //yo an if statement
			freq.insert({a[i] , 1});
		}
		else { //there you go an else one
			freq[a[i]]++;
		}
	}

	long long maxsize = 0; //some more variables
	long long majelem = -1; //some further more variables

	for (auto itr = freq.begin() ; itr != freq.end() ; ++itr) { //ok last for loop
		if (maxsize <= itr->second) { //and last conditional as well
			maxsize = itr->second;
			majelem = itr->first;
		}
	}

	std :: cout << min(2 * maxsize - 1 , n) << "\n" ; //ok finally a print statement
	return 0; //there you returned something
}
