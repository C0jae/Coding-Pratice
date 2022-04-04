package Programmers;
import java.util.Arrays;

public class P6_완주하지못한선수 {

    public static String solution(String[] participant, String completion[]) {
        Arrays.sort(participant);
        Arrays.sort(completion);

        int i;

        for (i = 0; i < completion.length; i++) {
            if (!participant[i].equals(completion[i]))
                break;
            }

        return participant[i];
    }

    public static void main(String[] arg) {
        String[] a = {"loe", "kiki", "eden", "kiki"};
        String[] b = {"eden", "kiki", };

        System.out.println(solution(a, b));
    }
}
