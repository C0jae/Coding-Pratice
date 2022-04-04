package Programmers;
import java.util.ArrayList;
import java.util.List;

public class P1_인형뽑기 {

    public static int solution(int[][] board, int[] moves) {
        int answer = 0;
        List<Integer> room = new ArrayList<Integer>();

        for (int i = 0; i < moves.length; i++) {
            for (int j = 0; j < board.length; j++) {
                if (board[j][moves[i] - 1] != 0) {
                    room.add(board[j][moves[i] - 1]);
                    board[j][moves[i] - 1] = 0;
                    break;
                }
            }
        }

        while (true) {
            int check = 0;
            System.out.println(room);
            for (int i = 1; i < room.size(); i++) {
                if (room.get(i) == room.get(i - 1)) {
                    answer += 2;
                    room.remove(i);
                    room.remove(i - 1);
                    check = 1;
                    break;
                }
            }
            System.out.println("check : " + check);
            if (check == 0)
                break;
        }
        return answer;
    }

    public static void main(String[] args) throws Exception {
        int[][] b = { { 0, 0, 0, 0, 0 }, { 0, 0, 1, 0, 3 }, { 0, 2, 5, 0, 1 }, { 4, 2, 4, 4, 2 }, { 3, 5, 1, 3, 1 } };
        int[] a = { 1, 5, 3, 5, 1, 2, 1, 4 };

        System.out.println("answer : " + solution(b, a));
    }
}

// stack 이용해서도 해보기
// stack.peek() / stack.pop() / stack.empty() = 최근내역 조회 / 최근내역 삭제 / 최근내역 비어있는지
// 확인
