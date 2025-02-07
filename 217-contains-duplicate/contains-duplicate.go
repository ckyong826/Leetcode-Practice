func containsDuplicate(nums []int) bool {
    list := make(map[int]struct{})
    for _,val := range nums {
        if _,hasNum := list[val];hasNum {
            return true
        }
        list[val] = struct{}{}
    }
    return false
}