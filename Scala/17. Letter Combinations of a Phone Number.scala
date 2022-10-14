object Solution {
val letters = Map(
  '2' -> "abc",
  '3' -> "def",
  '4' -> "ghi",
  '5' -> "jkl",
  '6' -> "mno",
  '7' -> "pqrs",
  '8' -> "tuv",
  '9' -> "wxyz"
)

def letterCombinations(digits: String): List[String] = {
  digits.length match {
    case 0 => List.empty
    case 1 => letters(digits.head).map(_.toString).toList
    case 2 =>
      val l1 = letters(digits(0)).map(_.toString).toList
      val l2 = letters(digits(1)).map(_.toString).toList
      getCombinations(l1, l2)
    case _ =>
      val lhead = letters(digits.head).map(_.toString).toList
      getCombinations(lhead, letterCombinations(digits.tail))
  }
}

def getCombinations(l1: List[String], l2: List[String]): List[String] = {
  val result =
    for {
      i <- l1.indices
      j <- l2.indices
    } yield {
      l1(i) + l2(j)
    }
  result.toList
}

}
