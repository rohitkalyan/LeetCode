object Solution {
  def romanToInt(s: String): Int = {
    val map= s.map(x => {
      x match {
        case 'I' => 1
        case 'V' => 5
        case 'X' => 10
        case 'L' => 50
        case 'C' => 100
        case 'D' => 500
        case 'M' => 1000
      }
    })
    var sum = 0
    for(i <- 0 until map.size -1){
      if(map(i) < map(i + 1)){
        sum += map(i) * -1
      }
      else {
        sum += map(i)
      }
    }
    println(map.last)
    sum + map.last
  }
}
