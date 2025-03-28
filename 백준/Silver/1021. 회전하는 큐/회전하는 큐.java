import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String[] x = br.readLine().split(" ");
        int N = Integer.parseInt(x[0]);
        int M = Integer.parseInt(x[1]);
        int[] numbers = new int[M];
        String[] numbersStr = br.readLine().split(" ");
        for (int i = 0; i < M; i++) {
            numbers[i] = Integer.parseInt(numbersStr[i]);
        }

        LinkedList<Integer> queue = new LinkedList<>();
        for (int i = 1; i < N+1; i++) {
            queue.offer(i);
        }

        int count = 0;
        for (int number : numbers) {
            count += check(queue, number);
        }
        sb.append(count);
        System.out.println(count);
        br.close();
    }

    public static int check(LinkedList<Integer> queue, int number) {
        int count = 0;
        while(true) {
            if (queue.getFirst() == number) {
                queue.pollFirst();
                return count;
            } else if (queue.indexOf(number) <= queue.size() / 2) {
                int pollNum = queue.pollFirst();
                queue.add(pollNum);
                count++;
            } else {
                int pollNum = queue.pollLast();
                queue.addFirst(pollNum);
                count++;
            }
        }
    }
}
