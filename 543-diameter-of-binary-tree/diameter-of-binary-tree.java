/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int maxD = 0;
    public int helper(TreeNode root){
            if (root==null){
                return 0;
            }
            int left = helper(root.left);
            int right = helper(root.right);
            maxD = Math.max(maxD,(left+right));
            return 1 + Math.max(left,right);
        }
    public int diameterOfBinaryTree(TreeNode root) {
        maxD = 0;
        helper(root);
        return maxD;
    }
}