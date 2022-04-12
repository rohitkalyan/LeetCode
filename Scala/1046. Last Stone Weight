object Solution {
  def lastStoneWeight(stones: Array[Int]): Int = {
    var stack = scala.collection.mutable.Stack[Int](stones:_*).reverse

    while(stack.size > 1){
      stack = stack.sorted.reverse
      val x = stack.pop()
      val y = stack.pop()
      stack.push((x - y).abs)
    }
      stack(0)
  }
}
