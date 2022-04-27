import scala.collection.mutable.HashSet
object Solution {
    def lengthOfLongestSubstring(s: String): Int = {
        var i = 0
        var j = 0
        var res  = 0
        val hash_Set = new HashSet[Char]()
        while(j < s.size){
            if(!hash_Set.contains(s.charAt(j))){
                hash_Set.add(s.charAt(j))
                res = Math.max(hash_Set.size, res)
                j += 1
            }
            else{
                hash_Set.remove(s.charAt(i))
                i += 1
            }
        }
        return res
        
    }
}
