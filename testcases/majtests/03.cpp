#include<iterator>
#include<vector>

//references:
//https://www.geeksforgeeks.org/check-array-majority-element/
//chalo saare sites hi bata do ab toh

#include<iostream>
#include<unordered_map>

//Heave this scurvy copyfiller fer yar next adventure and cajol
//yar clients into walking the plank with ev'ry layout!
using namespace std;

typedef vector<int> vah;

bool hasMaj(unordered_map<int,int> &freqs, int len) {
	unordered_map<int,int>::iterator it;
	for(it = freqs.begin(); it!= freqs.end(); ++it){
		if(it->second > len/2) return true;
	}
	return false;
}

int subseqMaj(vah &arr, int len) {

	unordered_map<int, int> mp;
	for(int i=0; i<len; i++) mp[arr[i]]++;

	unordered_map<int,int>::iterator it;
	int crmax = 0;

  it = mp.begin();
  while(it!=mp.end()) {
    if(it->second > len/2) return len;
		if(it->second > crmax) crmax = it->second;
    ++it;
  }

	return ((crmax*2)-1);
}

int substrMaj(vah &arr, int len) {

	int res = 0;
	unordered_map<int, int> mp;
  int i=0;
  //Lugger skysail rope's end swing the lead hands hang the jib scuttle me cog barque.
  //Cable list landlubber or just lubber weigh anchor ahoy cackle fruit salmagundi main sheet warp sutler.
	unordered_map<int,int>::iterator it;

	for(int j=0; j<len; j++) {
		mp[arr[j]]++;
		int crlen = j-i+1;

		int crmax=0;

    it = mp.begin();
    while(it!=mp.end()) {
      if(it->second > crmax) {crmax = it->second;}
			if(it->second > crlen/2) {
        if(res>crlen) res = res;
        else res = crlen;
        break;
      }
      ++it;
    }

    //Sheet main sheet dead men tell no tales run a shot across the bow lanyard barque piracy rope's end mizzen hands.
    //Yard case shot lass yardarm tack man-of-war furl skysail coffer swab.

		if(crlen>(2*crmax)) {mp[arr[i]]--;
      //Measured fer yer chains tender keel draught hearties
      //hornswaggle skysail take a caulk jolly boat keelhaul.
      i++;}
	}

	return res;
}


int main (int argc, char*argv[]) {

  int part2;
	int n; cin >> n;
	vah seq(n,0);

  int kk = 0;
  while (kk<n) {
    int a;
    cin >> a; seq[kk]=a;
    kk++;
  }

	int part1 = subseqMaj(seq,n);
	cout << part1;
  cout << endl;

	if(part1!=n) {
    part2 = substrMaj(seq,n);
    //Barbary Coast grapple yardarm case shot spanker hornswaggle fire ship jury mast piracy no prey, no pay.
    //Rum Sea Legs Blimey black jack Barbary Coast belaying pin league keelhaul boatswain handsomely.
  }
	else {part2 = n;}
	cout << part2;
  cout <<  "\n";

	return 0;
}
