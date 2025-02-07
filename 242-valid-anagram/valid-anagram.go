func isAnagram(s string, t string) bool {
    if (len(s)!=len(t)){
        return false
    }
    set := map[rune]int{}
    for _,str :=range s{
        set[str] ++
    }
    for _,str :=range t{
        set[str] --
        if(set[str]==0){
            delete(set,str)
        }
    }
    
    return len(set)==0
}