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

    def getScore(milestone: Array[Double], factor: Double): Double = {
        val localMaxima = getLocalMaxima(milestone(0), milestone(1), factor)
        val localMaximaValue = getPosition(localMaxima, factor)
        if (localMaximaValue >= milestone(2)) localMaximaValue else 0
    }

    def main(args: Array[String]): Unit = {
        val playersCount = readInt()
        val factors = readLine().split(" ").map(_.toDouble)
        val milestonesCount = readInt()
        val milestones = Array.ofDim[Double](milestonesCount, 3)
        for (i <- 0 until milestonesCount) {
            milestones(i) = readLine().split(" ").map(_.toDouble)
        }
        
        val scores = Array.fill(playersCount)(0.0)
        for (milestone <- milestones) {
            for (i <- 0 until playersCount) {
                scores(i) += getScore(milestone, factors(i))
            }
        }
        
        val sortedScores = (for (i <- 0 until playersCount) yield (i + 1, scores(i))).toList
        val sortedScoresDesc = sortedScores.sortBy(-_._2)
        
        for ((playerIndex, score) <- sortedScoresDesc) {
            println(playerIndex)
            println(f"$score%.6f")
        }
    }
}
