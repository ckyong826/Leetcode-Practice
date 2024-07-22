class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> heap;
        heap = new PriorityQueue<>(Collections.reverseOrder());

        for (int num:stones){
            heap.add(num);
        }

        while (heap.size()>1) {
            heap.add(heap.poll()-heap.poll());
        }
        return heap.peek();
    }
}