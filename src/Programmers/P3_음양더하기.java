package Programmers;
public class P3_음양더하기 {

    public static int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;

        for (int i = 0; i < absolutes.length; i++) {
            if (signs[i] == false)
                absolutes[i] *= -1;
            answer += absolutes[i];
        }

        return answer;
    }

    public static void main(String[] args) {
        boolean[] signs = { false, false, true };
        int[] absolutes = { 1, 2, 3 };

        System.out.println(solution(absolutes, signs));
    }

}
