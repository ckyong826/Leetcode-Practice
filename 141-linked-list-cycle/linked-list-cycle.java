/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head==null || head.next==null){
            return false;
        }
        // Solution 1 : HashTable
        HashMap<ListNode,Integer> map = new HashMap<>();
        while (head!=null){
            if (map.containsKey(head)){
                return true;
            }
            map.put(head,1);
            head=head.next;
        }
        return false;
    }
}