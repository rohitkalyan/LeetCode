object Solution {
  def twoSum(nums: Array[Int], target: Int): Array[Int] = {
    var resultArr = Array[Int]()
    var map: Map[Int, Int] = Map.empty[Int, Int]
    for(i <- 0 until nums.size){
      val rem = target - nums(i)
      if(map.contains(rem)){
        resultArr +:= i
        resultArr +:= map(rem)
      }
      else {
        map += (nums(i) -> i)
      }
    }
    resultArr
  }
}
