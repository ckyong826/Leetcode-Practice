func topKFrequent(nums []int, k int) []int {
    Map := map[int]int{}
    for _,val := range nums {
        Map[val] += 1 
    }
    type kv struct {
        key int
        val int
    }
    pairs := make([]kv,0)
    for k,v := range Map{
        pairs = append(pairs,kv{k,v})
    }

    sort.Slice(pairs,func(i,j int)bool{
        return pairs[i].val > pairs[j].val
    })
    ans := make([]int,0,k)
    for i:=0;i<k;i++ {
        ans = append(ans,pairs[i].key)
    }

    return ans
}