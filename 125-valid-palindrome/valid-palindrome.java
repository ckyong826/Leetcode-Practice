class Solution {
    public boolean isPalindrome(String s) {
        String cleanedString = s.replaceAll("[^a-zA-Z0-9]", "");
        cleanedString=cleanedString.toLowerCase();
        // Solution 1 : 2 Pointers
        char[] arrayS = cleanedString.toCharArray();
        int l  = 0;
        int r = cleanedString.length()-1;
        while (l < cleanedString.length()){
            if (arrayS[l]!=arrayS[r]){
                return false;
            }
            l++;
            r--;
        }
        return true;

    }
}