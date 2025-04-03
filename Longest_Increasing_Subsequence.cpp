//Given an integer array nums, return the length of the longest strictly increasing subsequence.
int lengthOfLIS(vector<int>& nums) {
        vector<int>sub;
        for(auto i : nums){
            auto it = lower_bound(sub.begin(),sub.end(),i);
            if(it==sub.end()){
                sub.push_back(i);
            }
            else{
                *it = i;
            }
        }
        return sub.size();
    }
