object Solution {
  def findMedianSortedArrays(nums1: Array[Int], nums2: Array[Int]): Double = {
    val com_Array = (nums1 ++ nums2).sorted
    if(com_Array.size % 2 != 0){
      return com_Array((com_Array.size / 2))
    }
    else{
      val pos1 = com_Array.size / 2
      return ((com_Array(pos1) + com_Array(pos1 - 1).toDouble) / 2)
    }
  }
}
