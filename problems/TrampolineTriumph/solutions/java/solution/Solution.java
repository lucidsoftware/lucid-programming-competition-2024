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

    public static double getJumpDistance(double[] milestone, double factor) {
        double localMaxima = getLocalMaxima(milestone[0], milestone[1], factor);
        return getPosition(localMaxima, factor);
    }

    public static int[] getScores(double[][] milestones, double[] factors) {
        int playersCount = factors.length;
        int[] scores = new int[playersCount];
        for (double[] milestone : milestones) {
            Double maxJumpDistance = null;
            Integer winner = null;
            for (int i = 0; i < playersCount; i++) {
                double jumpDistance = getJumpDistance(milestone, factors[i]);
                if (maxJumpDistance == null || jumpDistance > maxJumpDistance) {
                    maxJumpDistance = jumpDistance;
                    winner = i;
                } else if (jumpDistance == maxJumpDistance) {
                    System.err.println("Error: multiple winners");
                }
            }
            if (winner != null) {
                scores[winner]++;
            }
        }
        return scores;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int playersCount = scanner.nextInt();

        double[] factors = new double[playersCount];
        for (int i = 0; i < playersCount; i++) {
            factors[i] = scanner.nextDouble();
        }

        int milestonesCount = scanner.nextInt();
        double[][] milestones = new double[milestonesCount][2];
        for (int i = 0; i < milestonesCount; i++) {
            for (int j = 0; j < 2; j++) {
                milestones[i][j] = scanner.nextDouble();
            }
        }

        int[] scores = getScores(milestones, factors);
        List<int[]> sortedScores = new ArrayList<>();
        for (int i = 0; i < playersCount; ++i) {
            sortedScores.add(new int[]{i + 1, scores[i]});
        }
        sortedScores.sort((a, b) -> {
            int cmp = Integer.compare(b[1], a[1]);
            if (cmp != 0) {
                return cmp;
            }
            return Integer.compare(a[0], b[0]);
        });

        for (int[] score : sortedScores) {
            System.out.println(score[0] + " " + score[1]);
        }

        scanner.close();
    }
}
