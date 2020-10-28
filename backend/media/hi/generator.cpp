#include<iostream>
#include<vector>
using namespace std;
int main(){
freopen("input.txt", "w", stdout);
int n = 0;
int k = 100;
vector<int> values;
for (int i = 0; i < k; i++){
int r = (rand()%(200000/(max(1,k))));
values.push_back(r);
n += r;
}
cout << n << ' ' << k << endl;
for (int i = 0; i < k; i++)
cout << values[i] << ' ';
cout << endl;
return 0;

}