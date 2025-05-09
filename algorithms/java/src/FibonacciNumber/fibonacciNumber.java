
import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;

// 有序数组中是否存在一个数字
public class fibonacciNumber {
    public static void main(String[] args) {
        System.out.println("测试开始");
        // 定义测试用例：输入 -> 期望输出
        Map<Integer, Integer> testCases = new HashMap<>();
        testCases.put(0, 0);
        testCases.put(1, 1);
        testCases.put(2, 1);
        testCases.put(3, 2);
        testCases.put(4, 3);
        testCases.put(5, 5);
        testCases.put(6, 8);

        // 运行测试
        for (Map.Entry<Integer, Integer> entry : testCases.entrySet()) {
            int input = entry.getKey();
            int expected = entry.getValue();
            int actual = fib2(input);
            String result = (actual == expected) ? "✅ 成功" : "❌ 失败，期望: " + expected + ", 实际: " + actual;
            System.out.println("输入: " + input + " => 输出: " + actual + " => " + result);
        }
        System.out.println("测试结束");
    }

    // 1、暴力递归
    public static int fib1(int n) {
        return f1(n);
    }

    public static int f1(int i) {
        if (i == 0) {
            return 0;
        }
        if (i == 1) {
            return 1;
        }
        return f1(i - 1) + f1(i - 2);
    }

    // 2、动态规划（记忆式搜索）
    public static int fib2(int n) {
        int[] dp = new int[n + 1];
        Arrays.fill(dp, -1);
        return f2(n, dp);
    }

    public static int f2(int i, int[] dp) {
        if (i == 0) {
            return 0;
        }
        if (i == 1) {
            return 1;
        }
        if (dp[i] != -1) {
            return dp[i];
        }
        int ans = f2(i - 1, dp) + f2(i - 2, dp);
        dp[i] = ans;
        return ans;
    }


    // 3、动态规划（表格填充法）
    public static int fib3(int n) {
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        int[] dp = new int[n + 1];
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }

    // 4、滚动数组
    public static int fib4(int n) {
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        int lastLast = 0, last = 1;
        for (int i = 2, cur; i <= n; i++) {
            cur = lastLast + last;
            lastLast = last;
            last = cur;
        }
        return last;
    }
}



