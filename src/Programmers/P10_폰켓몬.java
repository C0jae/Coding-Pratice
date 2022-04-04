package Programmers;
import java.util.Arrays;

public class P10_폰켓몬 {
    
    public static int solution(int[] nums) {
        int answer = 1;

        Arrays.sort(nums);

        for (int i = 1; i < nums.length; i++) {
            if (nums[i-1] != nums[i]) answer++;
        }
        
        if (answer > nums.length / 2) answer = nums.length / 2;

        return answer;
    }

    public static void main(String[] args) {
        int[] nums = {3, 1, 2, 3};

        System.out.println(solution(nums));
    }
}
