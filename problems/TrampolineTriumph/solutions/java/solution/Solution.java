import java.util.*;
import java.lang.Math;

public class Solution {
    
    public static double getPosition(double x, double factor) {
        return (6 - 2 * factor * Math.sin(x / 2) 
                  - 2 * factor * Math.sin(x / 5) 
                  - 2 * factor * Math.sin(x / 7)) * (0.9 + (1 + Math.sin(x * factor / 3)) / 20);
    }

    public static double getLocalMaxima(double l, double r, double factor) {
        while (r - l > 1e-9) {
            double m1 = l + (r - l) / 3;
            double m2 = r - (r - l) / 3;
            if (getPosition(m1, factor) > getPosition(m2, factor)) {
                r = m2;
            } else {
                l = m1;
            }
        }
        return l;
    }

    public static double getScore(double[] milestone, double factor) {
        double localMaxima = getLocalMaxima(milestone[0], milestone[1], factor);
        double localMaximaValue = getPosition(localMaxima, factor);
        return localMaximaValue >= milestone[2] ? localMaximaValue : 0;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int playersCount = scanner.nextInt();

        double[] factors = new double[playersCount];
        for (int i = 0; i < playersCount; ++i) {
            factors[i] = scanner.nextDouble();
        }
        
        int milestonesCount = scanner.nextInt();
        double[][] milestones = new double[milestonesCount][3];
        for (int i = 0; i < milestonesCount; ++i) {
            for (int j = 0; j < 3; ++j) {
                milestones[i][j] = scanner.nextDouble();
            }
        }
        
        double[] scores = new double[playersCount];
        for (double[] milestone : milestones) {
            for (int i = 0; i < playersCount; ++i) {
                scores[i] += getScore(milestone, factors[i]);
            }
        }
        
        List<double[]> sortedScores = new ArrayList<>();
        for (int i = 0; i < playersCount; ++i) {
            sortedScores.add(new double[]{i + 1, scores[i]});
        }

        sortedScores.sort((a, b) -> Double.compare(b[1], a[1]));

        for (double[] score : sortedScores) {
            System.out.println((int)score[0]);
            System.out.printf("%.6f%n", score[1]);
        }
        
        scanner.close();
    }
}
