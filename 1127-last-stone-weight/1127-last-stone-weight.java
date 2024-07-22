class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> heap;
        heap = new PriorityQueue<>();

        for (int num:stones){
            heap.add(-num);
        }

        while (heap.size()>1) {
            int a = heap.poll();
            int b = heap.poll();
            int temp=a-b;
            heap.offer(temp);
        }
        return -heap.peek();
    }
}