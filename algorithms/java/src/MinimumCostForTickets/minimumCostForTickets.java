
import java.util.*;

// 有序数组中是否存在一个数字
public class minimumCostForTickets {
    // 测试用例封装类
    static class TestCase {
        int[] days;
        int[] costs;
        int expected;

        TestCase(int[] days, int[] costs, int expected) {
            this.days = days;
            this.costs = costs;
            this.expected = expected;
        }
    }

    // 无论提交什么方法都带着这个数组      0  1  2
    public static int[] durations = { 1, 7, 30 };
    public static void main(String[] args) {
        System.out.println("测试开始");

        // 定义测试用例：输入 -> 期望输出
        List<TestCase> testCases = new ArrayList<>();

        // 示例 1:
        testCases.add(new TestCase(
                new int[]{1,4,6,7,8,20},  // days
                new int[]{2, 7, 15},              // costs
                11                              // expected
        ));

        // 示例 2:
        testCases.add(new TestCase(
                new int[]{1,2,3,4,5,6,7,8,9,10,30,31},
                new int[]{2, 7, 15},
                17
        ));

        for (TestCase t : testCases) {
            int actual = mincostTickets1(t.days, t.costs);
            String result = (actual == t.expected) ? "✅ 成功" : "❌ 失败，期望: " + t.expected + ", 实际: " + actual;
            System.out.println("输入: " + Arrays.toString(t.days) +
                    " | Costs: " + Arrays.toString(t.costs) +
                    " => 输出: " + actual +
                    " => " + result);
        }

        System.out.println("测试结束");
    }

    // 暴力尝试
    public static int mincostTickets1(int[] days, int[] costs) {
        return f1(days, costs, 0);
    }

    // days[i..... 最少花费是多少
    public static int f1(int[] days, int[] costs, int i) {
        if (i == days.length) {
            // 后续已经无旅行了
            return 0;
        }
        // i下标 : 第days[i]天，有一场旅行
        // i.... 最少花费是多少
        int ans = Integer.MAX_VALUE;
        for (int k = 0, j = i; k < 3; k++) {
            // k是方案编号 : 0 1 2
            while (j < days.length && days[i] + durations[k] > days[j]) {
                // 因为方案2持续的天数最多，30天
                // 所以while循环最多执行30次
                // 枚举行为可以认为是O(1)
                j++;
            }
            ans = Math.min(ans, costs[k] + f1(days, costs, j));
        }
        return ans;
    }

    // 暴力尝试改记忆化搜索
    // 从顶到底的动态规划
    public static int mincostTickets2(int[] days, int[] costs) {
        int[] dp = new int[days.length];
        for (int i = 0; i < days.length; i++) {
            dp[i] = Integer.MAX_VALUE;
        }
        return f2(days, costs, 0, dp);
    }

    public static int f2(int[] days, int[] costs, int i, int[] dp) {
        if (i == days.length) {
            return 0;
        }
        if (dp[i] != Integer.MAX_VALUE) {
            return dp[i];
        }
        int ans = Integer.MAX_VALUE;
        for (int k = 0, j = i; k < 3; k++) {
            while (j < days.length && days[i] + durations[k] > days[j]) {
                j++;
            }
            ans = Math.min(ans, costs[k] + f2(days, costs, j, dp));
        }
        dp[i] = ans;
        return ans;
    }

    // 严格位置依赖的动态规划
    // 从底到顶的动态规划
    public static int MAXN = 366;

    public static int[] dp = new int[MAXN];

    public static int mincostTickets3(int[] days, int[] costs) {
        int n = days.length;
        Arrays.fill(dp, 0, n + 1, Integer.MAX_VALUE);
        dp[n] = 0;
        for (int i = n - 1; i >= 0; i--) {
            for (int k = 0, j = i; k < 3; k++) {
                while (j < days.length && days[i] + durations[k] > days[j]) {
                    j++;
                }
                dp[i] = Math.min(dp[i], costs[k] + dp[j]);
            }
        }
        return dp[0];
    }

}



