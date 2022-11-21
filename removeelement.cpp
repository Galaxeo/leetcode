class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int retsize = nums.size();
        for (size_t i = 0; i < nums.size(); i++) {
            if (nums[i] == val) {
                nums[i] = 101;
                retsize-=1;
            }
        }
        sort(nums.begin(), nums.end());
        return retsize;
    }
};