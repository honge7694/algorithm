import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static void input() throws Exception {
        /** 시간초과
        int N = scan.nextInt();
        List<Integer> myCards = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            myCards.add(scan.nextInt());
        }
        Collections.sort(myCards);

        int M = scan.nextInt();
        List<Integer> cards = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            cards.add(scan.nextInt());
        }

        int[] answer = new int[M];
        int middleCard = myCards.size() / 2;
        for (int i = 0; i < M; i++) {
            if (cards.get(i) > myCards.get(middleCard)) {
                List<Integer> bigCard = myCards.subList(middleCard, N);
                for (int card : bigCard) {
                    if (cards.get(i) == card) {
                        answer[i] = 1;
                        break;
                    }
                }
            } else {
                List<Integer> smallCard = myCards.subList(0, middleCard);
                for (int card : smallCard) {
                    if (cards.get(i) == card) {
                        answer[i] = 1;
                        break;
                    }
                }
            }
        }

        for (int ans : answer) {
            sb.append(ans).append(' ');
        }
        */

        int N = scan.nextInt();
        HashMap<String, Integer> myCards = new HashMap<>();
        for (int i = 0; i < N; i++) {
            myCards.put(scan.next(), 0);
        }

        int M = scan.nextInt();
        List<Integer> cards = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            cards.add(scan.nextInt());
        }

        int[] answer = new int[M];
        for (int i = 0; i < cards.size(); i++) {
            if (myCards.containsKey(cards.get(i).toString())) {
                answer[i] = 1;
            }
        }

        for (int ans : answer) {
            sb.append(ans).append(' ');
        }

        print();
    }

    static void print() {
        System.out.print(sb.toString());
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public FastReader(String s) throws FileNotFoundException {
            br = new BufferedReader(new FileReader(new File(s)));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }

    public static void main(String[] args) throws Exception {
        input();
    }

    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

}