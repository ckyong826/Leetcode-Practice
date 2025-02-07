func groupAnagrams(strs []string) [][]string {
    set := make(map[string][]string)
    for _,str := range strs{
        chars := strings.Split(str, "")
        sort.Strings(chars)
        key := strings.Join(chars, "")
        set[key] = append(set[key], str)
    }

    answer := make([][]string, 0, len(set))
    for _,val := range set{
        answer = append(answer,val)
    }
    return answer
}