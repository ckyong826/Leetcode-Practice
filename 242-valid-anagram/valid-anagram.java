class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length()!=t.length()){
            return false;
        }
        // Solution 1 : HashMap
        // HashMap<Character,Integer> sCount = new HashMap<>();
        // HashMap<Character,Integer> tCount = new HashMap<>();
        // for (int i=0;i<s.length();i++){
        //     sCount.put(s.charAt(i),sCount.getOrDefault(s.charAt(i),0)+1);
        //     tCount.put(t.charAt(i),tCount.getOrDefault(t.charAt(i),0)+1);
        // }
        // return sCount.equals(tCount);

        // Solution 2 : Sort
        char[] sortedS = s.toCharArray();
        Arrays.sort(sortedS);
        char[] sortedT = t.toCharArray();
        Arrays.sort(sortedT);
        for (int i=0;i<s.length();i++){
            if (sortedS[i]!=sortedT[i]){
                return false;
            }
        }
        return true;
    }
}