#include<iostream>
#include<cmath>
#include<map>
#include<algorithm>
#include<vector>

void function(int aaaa, int bbbb, int cccc){ //it's ain't gonna be used
	int dddd=aaaa; //some more variables
	aaaa=bbbb;
	bbbb=cccc; //this is just a comment
	cccc=dddd;
}

void func(int xxxx, int yyyy, int zzzz){ //this one neither
	int qqqq=zzzz; //some more variables
	zzzz=yyyy; //this is just a comment
	yyyy=xxxx;
	xxxx=qqqq; //this is just a comment
}

int main(){
	long long m; //this is a variable
	std :: cin >> m; //this is input statement
	long long arr[m]; //this is an array

	int qwert=100; //this is an unused variable
	long long yuiop=1234567890; //this is just a comment

	long long j = 0; //some further more variables
	func(1,2,3); //an unused function

	while (j < m) { //this is a while loop
		std :: cin >> arr[j];
		j++; //this is just a comment
	}

	function(1,2,3); //another unused function
	std :: map<long long , long long> count; //this is a map

	char asdfg='c'; //some further more variables
	string hjkl="qwertyuiop asdfghjkl zxcvbnm"; //this is just a comment

	j = 0; //some further more variables
	func(4,5,6); //another unused function

	while (j < m) { //another while loop?
		switch (count.find(arr[j]) == count.end()) { //yo a switch statement
			case true: //there you go a case one
				count.insert({arr[j] , 1});
			case false:
				count[arr[j]]++; //this is just a comment
		}
		j++;
	}

	function(4,5,6); //another unused function
	long long alpha = 0; //some more variables
	long long beta = -1; //some further more variables

	float zxcv=12345.09876; //this is just a comment
	boolean yes=true; //some further more variables
	double bnm=1234567890.0987654321; //this is an unused variable

	auto gamma = count.begin(); //some further more variables
	func(7,8,9); //another unused function

	while (gamma != count.end()) { //ok last while loop
		switch (alpha <= gamma->second) { //and last conditional as well
			case true:
				alpha = gamma->second;
				beta = gamma->first; //this is just a comment
		}
		++gamma;
	}

	function(7,8,9); //another unused function
	std :: cout << min(2 * alpha - 1 , m) << "\n" ; //ok finally a print statement
	return 0; //there you returned something
}
