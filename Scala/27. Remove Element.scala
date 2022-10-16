object Solution {
    def removeElement(nums: Array[Int], n: Int): Int = {
            var res = nums.filter(_ != n)
            var len = res.size
            for( i <- 0 until len)
              nums(i) = res(i)
            return len
    }
}
