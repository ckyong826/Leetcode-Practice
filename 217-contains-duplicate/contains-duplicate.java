class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> ans = new HashSet<Integer>();
        for(int num:nums){
            if (ans.contains(num)){
                return true;
            }
            ans.add(num);
        }
        return false;
    }
}