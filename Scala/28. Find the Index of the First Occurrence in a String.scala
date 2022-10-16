object Solution {
    def strStr(haystack: String, needle: String): Int = {
            var ind = 0
            if(haystack.contains(needle)){
              ind = haystack.indexOf(needle)
            }
            else{
                ind = -1
            }
            ind
    }
}
