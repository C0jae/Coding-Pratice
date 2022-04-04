package Programmers;
import java.util.ArrayList;

public class P13_3진법뒤집기 {
    
    public static int solution(int n) {
        int answer = 0;
        ArrayList<Integer> temp = new ArrayList<>();

        while(true) {
            if (n < 3) {
                temp.add(n);
                break;
            }

            temp.add(n % 3);
            n = n / 3;
        }

        for (int i = 0; i < temp.size(); i++) {
            answer += Math.pow(3, temp.size() -i -1) * temp.get(i);
        }


        return answer;
    }

    public static void main(String[] args) {
        int n = 45;

        System.out.println(solution(n));
    }
}
