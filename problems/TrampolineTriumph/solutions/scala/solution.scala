import scala.io.StdIn._
import scala.math._

object Solution {
    
  def getPosition(x: Double, factor: Double): Double = {
    (6 - 2 * factor * sin(x / 2)
      - 2 * factor * sin(x / 5)
      - 2 * factor * sin(x / 7)) * (0.9 + (1 + sin(x * factor / 3)) / 20)
  }

  def getLocalMaxima(l: Double, r: Double, factor: Double): Double = {
    var left = l
    var right = r
    while (right - left > 1e-9) {
      val m1 = left + (right - left) / 3
      val m2 = right - (right - left) / 3
      if (getPosition(m1, factor) > getPosition(m2, factor)) {
        right = m2
      } else {
        left = m1
      }
    }
    left
  }

  def getJumpDistance(milestone: Array[Double], factor: Double): Double = {
    val localMaxima = getLocalMaxima(milestone(0), milestone(1), factor)
    getPosition(localMaxima, factor)
  }

  def getScores(milestones: Array[Array[Double]], factors: Array[Double]): Array[Int] = {
    val playersCount = factors.length
    val scores = Array.fill(playersCount)(0)
    for (milestone <- milestones) {
      var maxJumpDistance: Option[Double] = None
      var winner: Option[Int] = None
      for (i <- 0 until playersCount) {
        val jumpDistance = getJumpDistance(milestone, factors(i))
        if (maxJumpDistance.isEmpty || jumpDistance > maxJumpDistance.get) {
          maxJumpDistance = Some(jumpDistance)
          winner = Some(i)
        } else if (jumpDistance == maxJumpDistance.get) {
          println("Error: multiple winners")
        }
      }
      winner.foreach(w => scores(w) += 1)
    }
    scores
  }

  def main(args: Array[String]): Unit = {
    val playersCount = scala.io.StdIn.readInt()
    val factors = scala.io.StdIn.readLine().split(" ").map(_.toDouble)
    val milestonesCount = scala.io.StdIn.readInt()
    val milestones = Array.ofDim[Double](milestonesCount, 2)
    for (i <- 0 until milestonesCount) {
      milestones(i) = scala.io.StdIn.readLine().split(" ").map(_.toDouble)
    }

    val scores = getScores(milestones, factors)
    val sortedScores = scores.zipWithIndex.sortBy { case (score, index) => (-score, index) }

    for ((score, index) <- sortedScores) {
      println(s"${index + 1} $score")
    }
  }
}
