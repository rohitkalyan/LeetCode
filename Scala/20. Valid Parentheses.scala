import scala.collection.mutable


object Solution {
  def isValid(s: String): Boolean = {
    var stack = mutable.Stack[Char]()
    for(i <- 0 until(s.size)){
      if(!stack.isEmpty) {
        if (s.charAt(i).equals(')') && stack.top == '(') {
          stack.pop()
        }
        else if (s.charAt(i).equals('}') && stack.top == '{') {
          stack.pop()
        }
        else if (s.charAt(i).equals(']') && stack.top == '[') {
          stack.pop()
        }
        else {
          stack.push(s.charAt(i))
        }
      }
      else{
        stack.push(s.charAt(i))
      }
    }

    println(stack)

    if(stack.isEmpty){
      true
    }
    else {
        false
    }
}
 }
