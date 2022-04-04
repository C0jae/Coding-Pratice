package Programmers;
import java.util.ArrayList;
import java.util.Arrays;

public class P15_두개뽑아서더하기 {

    public static int[] solution(int[] numbers) {
        ArrayList<Integer> result = new ArrayList<>();

        for (int i = 0; i < numbers.length - 1; i++) {
            for(int j = i+1; j < numbers.length; j++) {
                int sum = numbers[i] + numbers[j];
                if (result.contains(sum)) continue;
                else result.add(sum);
            }
        }

        int[] answer = new int[result.size()];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = result.get(i);
        }

        Arrays.sort(answer);
    
        return answer;
    }

    public static void main(String[] args) {
        int[] numbers = {2, 1, 3, 4, 1};
        System.out.println(Arrays.toString(solution(numbers)));
    }
    
}
