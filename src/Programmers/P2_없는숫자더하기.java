package Programmers;
public class P2_없는숫자더하기 {

    public static int solution(int[] numbers) {
        int sum = 0;

        for (int i = 0; i < 10; i++) {
            sum += i;
        }

        for (int i = 0; i < numbers.length; i++) {
            sum -= numbers[i];
        }

        return sum;
    }

    public static void main(String[] args) {
            int[] numbers = {1,2,3,4,5};

            System.out.println(solution(numbers));
    }


    
}