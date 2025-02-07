func groupAnagrams(strs []string) [][]string {
    set := make(map[string][]string)
    for _,str := range strs{
        runes := []rune(str)
        sort.Slice(runes, func(i, j int) bool {
		    return runes[i] < runes[j]
	    })
        sortedStr := string(runes)
        set[sortedStr] = append(set[sortedStr], str)
    }

    answer := make([][]string, 0)
    for _,val := range set{
        answer = append(answer,val)
    }
    return answer
}