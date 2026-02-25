#include <bits/stdc++.h>
using namespace std;
void cac(vector<int>& nums){
    sort(nums.begin(),nums.end());
    int n = nums.size();
    int half = n/2;
    int basic = nums[half];
    int ans = 0;
    for(int i = 0 ; i < n ; i++){
        ans+=abs(nums[i] - basic);
    }
    cout << ans << endl;
}
int main(){
    int n;
    cin >> n;
    for(int i = 0 ; i < n ; i++){
        int a;
        cin >> a;
        vector<int> nums(a);
        for(int j = 0 ; j < a;j++){
            cin >> nums[j];
        }
        cac(nums);
    }
}