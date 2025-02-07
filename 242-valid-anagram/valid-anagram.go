func isAnagram(s string, t string) bool {
    if (len(s)!=len(t)){
        return false
    }
    setS := make(map[rune]int)
    setT := make(map[rune]int)
    for _,str :=range s{
        setS[str] ++
    }
    for _,str :=range t{
        setT[str] ++
    }
    for key,val := range setS {
        if val!=setT[key]{
            return false
        }
    }
    return true
}