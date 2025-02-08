func isValid(s string) bool {
    stack := []rune{}
    p := map[rune]rune{
        '(':')',
        '{':'}',
        '[':']',
    }
    for _,val := range s {
       if _, exist := p[val]; exist {
            stack = append(stack,val)
       } else {
            if len(stack)==0 || val != p[stack[len(stack)-1]]{
                return false
            }
            stack = stack[:len(stack)-1]
       }
    }
    return len(stack)==0
}