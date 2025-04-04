int longestConsecutive(vector<int>& nums) {
        unordered_set<int>s(nums.begin(),nums.end());
        int currstreak = 0;
        int longest = 0;
        for(auto i : s){
            if(s.find(i-1)==s.end()){
                currstreak = 1;
                while(s.find(i+1)!=s.end()){
                    currstreak++;
                    i++;
                }
                longest = max(longest,currstreak);
            }
        }
        return longest;
    }
