class Solution {
    public boolean isValid(String s) {
        // Solution 1 : Stack
        Stack<Character> stack = new Stack<>();
        stack.push(s.charAt(0));
        for (int i=1;i<s.length();i++){
            char open = ' ';
            if(!stack.empty()){
                open=stack.peek();
            }
            char close=s.charAt(i);
            if ((open=='(')&&(close==')')){
                stack.pop();
            }else if ((open=='[')&&(close==']')){
                stack.pop();
            }else if ((open=='{')&&(close=='}')){
                stack.pop();
            }else{
                stack.push(s.charAt(i));
            }
        }
        return stack.empty();

    }
}