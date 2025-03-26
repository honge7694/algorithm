import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());

        // 목표 수열을 입력받습니다.
        int[] goalSequence = new int[n];
        for (int i = 0; i < n; i++) {
            goalSequence[i] = Integer.parseInt(br.readLine());
        }

        int i = 1;  // `push` 할 수 있는 가장 작은 값
        Stack<Integer> stack = new Stack<>();
        boolean possible = true;

        // 목표 수열을 하나씩 확인하면서
        for (int target : goalSequence) {
            // target을 목표로 할 때까지 i를 push
            while (i <= target) {
                stack.push(i++);
                sb.append("+\n");
            }

            // stack의 top이 목표값과 같으면 pop
            if (stack.peek() == target) {
                stack.pop();
                sb.append("-\n");
            } else {
                // 목표 값이 stack top과 다르면 불가능
                possible = false;
                break;
            }
        }

        // 불가능한 경우 "NO"
        if (!possible) {
            sb.setLength(0);  // StringBuilder 초기화
            sb.append("NO");
        }

        System.out.print(sb);
        br.close();
    }
}