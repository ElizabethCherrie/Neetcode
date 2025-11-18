// 1437. Check If All 1's Are at Least Length K Places Away
// Given an binary array nums and an integer k, return true if all 
// 1's are at least k places away from each other, otherwise return false.

#include <vector>

class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        
        int isWrong = 0;

        for (int i = 0; i < nums.size(); i++){
            
            if ((nums[i] == 1) && isWrong){
                return false;
            } 
            
            if (isWrong > 0) {
                isWrong--;
            }

            if (nums[i] == 1 && !isWrong) {
                isWrong = k;
            }

        }
        return true;
    }
};