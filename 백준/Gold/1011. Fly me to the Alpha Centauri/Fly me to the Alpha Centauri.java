import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();

        for (int i = 0; i < T; i++) {
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            int distance = y - x;
            int moveCount = (int)Math.sqrt(distance);

            if (moveCount == Math.sqrt(distance)) {
                System.out.println(moveCount * 2 - 1);
            } else if (distance <= moveCount * moveCount + moveCount) {
                System.out.println(moveCount * 2);
            } else {
                System.out.println(moveCount * 2 + 1);
            }
        }
        scanner.close();
    }
}