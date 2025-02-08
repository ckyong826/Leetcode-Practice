func isPalindrome(s string) bool {
    var filtered []rune
	for _, char := range strings.ToLower(s) {
		if unicode.IsLetter(char) || unicode.IsDigit(char) {
			filtered = append(filtered, char)
		}
	}

    left,right:=0,len(filtered)-1
    for left < right{
        if filtered[left]!=filtered[right]{
            return false
        }
        left++
        right--
    }
    return true
}