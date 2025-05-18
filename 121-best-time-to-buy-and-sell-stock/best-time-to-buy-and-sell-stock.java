class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        if (n==0){
            return 0;
        }
        // Solution 1 : DP
        int min = 0;
        int maxProfit = 0;
        for (int i=1;i<n;i++){
            if (prices[i]<prices[min]){
                min = i;
                continue;
            } 
            int profit = prices[i]-prices[min];
            maxProfit = Math.max(maxProfit,profit);
        }
        return maxProfit;
    }
}