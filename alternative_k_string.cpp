#include <bits/stdc++.h>
using namespace std;
int main(){
	int k;
	cin >> k;
	string s;
	cin >> s;
	int n = s.size();
	vector<int>lower(n,0);
	vector<int>upper(n,0);
	if(isupper(s[0])){
		upper[0]++;
	} else {
		lower[0]++;
	}
	for(int i = 1 ; i < n ; i++){
		if(isupper(s[i])){
			upper[i] = upper[i-1] + 1;
		} else {
			lower[i] = lower[i-1] + 1;
		}
	}	
	int current = 0;
	int max_ans = 0;
	vector<int> dp(n,0);
//	for(int i = 0 ; i < n ; i++){
//		cout << lower[i] ; 
//	}
//	cout << endl;
//	for(int i = 0 ; i < n ; i++){
//		cout << upper[i] ; 
//	}
//	cout << endl;
	for(int i = 0 ; i < n ; i++){
		if(lower[i] >= k){
			if(current && ((i-k)>=0) && upper[i-k] >= k) {
				dp[i] = dp[i-k] + k;
			} else {
				dp[i] = k;
			}
			current = 0;
		} else if(upper[i] >= k){
			if(!current && ((i-k)>=0)&& lower[i-k] >= k){
				dp[i] = dp[i-k] + k;
			} else {
				dp[i] = k;
			}
			current = 1;
		}
	}
//	for(int i = 0 ; i < n ; i++){
//		cout << dp[i] ; 
//	}
	//cout << endl;
	cout << *max_element(dp.begin(),dp.end());
}
