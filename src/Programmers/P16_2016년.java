public class P16_2016년 {

    public static String solution(int a, int b) {
        String answer = null;
        String[] day = {"FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"};
        int[] date = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int allDate = 0;

        for (int i = 0; i < a - 1; i++) {
            allDate += date[i];
        }

        allDate += b - 1;

        answer = day[allDate % 7];

        return answer;
    }

    public static void main(String[] args) {
        int a = 5;
        int b = 24;

        System.out.println(solution(a, b));
    }
    
}
