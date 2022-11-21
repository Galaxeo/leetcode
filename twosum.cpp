class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int a = 0;
        int b = 0;
        for (int i = 0; i<nums.size(); i ++) {
            for (int z = i+1; z<nums.size(); z++) {
                if (nums[i] + nums[z] == target) {
                    a = i;
                    b = z;
                }
            }
        }
        return {a, b};
    }
};