import java.util.*;
import java.io.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        // Fast input reading
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // Read number of available training sessions S
        int S = Integer.parseInt(br.readLine().trim());

        // Read number of athlete applicants A
        int A = Integer.parseInt(br.readLine().trim());

        // Read training times X_a
        st = new StringTokenizer(br.readLine());
        int[] trainingTimes = new int[A];
        for (int i = 0; i < A; i++) {
            trainingTimes[i] = Integer.parseInt(st.nextToken());
        }

        // Read GAUGE improvements Y_a
        st = new StringTokenizer(br.readLine());
        int[] improvements = new int[A];
        for (int i = 0; i < A; i++) {
            improvements[i] = Integer.parseInt(st.nextToken());
        }

        // Initialize DP array
        // dp[j] will store the maximum GAUGE improvement achievable with j training sessions
        // Initialize with 0 as initially, no improvement is achieved
        int[] dp = new int[S + 1];

        for (int i = 0; i < A; i++) {
            int time = trainingTimes[i];
            int improvement = improvements[i];

            // Traverse the DP array from S down to time to ensure each athlete is only considered once
            for (int j = S; j >= time; j--) {
                dp[j] = Math.max(dp[j], dp[j - time] + improvement);
            }
        }

        // Find the maximum improvement achievable within S training sessions
        int maxImprovement = 0;
        for (int j = 0; j <= S; j++) {
            if (dp[j] > maxImprovement) {
                maxImprovement = dp[j];
            }
        }

        // Output the maximum sum of GAUGE improvements
        System.out.println(maxImprovement);
    }
}
