package Programmers;
public class P12_약수와개수의덧셈 {

    public static int solution(int left, int right) {

        int answer = 0;
        
        for (int i = left; i <= right; i++) {
            // 제곱수의 경우 약수의 개수는 모두 홀수
            if (i % Math.sqrt(i) == 0) answer -= i;

            // 제곱수가 아닌경우 약수의 개수는 모두 짝수
            else answer += i;
        }

        return answer;
    }

    public static void main(String[] args) {
        int left = 13;
        int right = 17;

        System.out.println(solution(left, right));
    }

}
