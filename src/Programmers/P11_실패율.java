package Programmers;
import java.util.*;

public class P11_실패율 {

    public static int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        int demo = stages.length;
        int mole;
        // double[] fail = new double[N];

        Arrays.sort(stages);

        for (int i = 1; i <= N; i++) {
            mole = 0;

            for (int j = 0; j < stages.length; j++) {
                if (i == stages[j]) mole++;
            }

            answer[i-1] = ((1000*mole) / demo);
            demo -= mole;
        }


        // int[] result = new int[N];

        for (int i = 0; i < N; i++) {
            for (int j = 1; j < N; j++) {
                if (answer[j-1] >= answer[j]) {

                }
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        int N = 5;
        int[] stages = {2, 1, 2, 6, 2, 4, 3, 3};

        System.out.println(Arrays.toString(solution(N, stages)));
    }
}