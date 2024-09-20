import java.util.*;

public class Solution {
    public int mincostMembership(int[] days, int[] costs) {
        Deque<int[]> sevenDays = new ArrayDeque<>();
        Deque<int[]> thirtyDays = new ArrayDeque<>();
        int totalCost = 0;

        // if I have to train today, the min cost today is a minimum of
        // - yesterday's cost plus single-day membership
        // - cost for 8 days ago plus 7-day membership
        // - cost 31 days ago plus 30-day membership
        for (int day : days) {
            // remove expired ticket
            while (!sevenDays.isEmpty() && sevenDays.peekFirst()[0] <= day - 7) sevenDays.pollFirst();
            while (!thirtyDays.isEmpty() && thirtyDays.peekFirst()[0] <= day - 30) thirtyDays.pollFirst();

            // purchase new ticket
            sevenDays.offerLast(new int[]{day, totalCost + costs[1]});
            thirtyDays.offerLast(new int[]{day, totalCost + costs[2]});

            totalCost = Math.min(totalCost + costs[0], Math.min(sevenDays.peekFirst()[1], thirtyDays.peekFirst()[1]));
        }

        return totalCost;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int[] days = Arrays.stream(scan.nextLine().split("\\s+"))
                .mapToInt(Integer::parseInt)
                .toArray();
        int[] costs = Arrays.stream(scan.nextLine().split("\\s+"))
                .mapToInt(Integer::parseInt)
                .toArray();

        Solution solution = new Solution();
        System.out.println(solution.mincostMembership(days, costs));
    }
}