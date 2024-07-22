class Solution {
    class Pair {
        int x;
        int y;
        double D;

        Pair(int x, int y, double D){
            this.x=x;
            this.y=y;
            this.D=D;
        }
    }

    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<Pair> heap = new PriorityQueue<>((a,b)-> Double.compare(b.D,a.D));
        for (int[] p : points){
            double d = Math.sqrt(Math.pow(p[0],2)+Math.pow(p[1],2));
            heap.offer(new Pair(p[0],p[1],d));
            if (heap.size()>k){
            heap.poll();
        }
        }
        
        int [][] res = new int [k][2];
        for (int i=0;i<k;i++){
            Pair pair = heap.poll();
            res[i][0] = pair.x;
            res[i][1] = pair.y;
        }
        return res;
    }
}