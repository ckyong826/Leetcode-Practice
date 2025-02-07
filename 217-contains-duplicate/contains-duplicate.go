func containsDuplicate(nums []int) bool {
    list := make(map[int]int)
    for _,val := range nums {
        list[val] += 1
        if list[val] > 1 {
            return true
        }
    }
    return false
}