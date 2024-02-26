import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    // 2 3 4 5 6 7
    // 3 5 7

    // 2 3 4 5 6 7 8 9 10 11 12 13 14 15 # 2로 7개 지움
    // 3 5 7 9 11 13 15 # 3으로 3개 지움
    // 5 7 11 13 # 5로 1개 지움
    // 11 13 # 7로 1개 지움

    static void input() throws Exception {
        int N = scan.nextInt();
        int K = scan.nextInt();
        List<Integer> numbers = new ArrayList<>();
        int P = 0;
        int count = 0;
        int answer = 0;

        for (int i = 2; i <= N; i++) {
            numbers.add(i);
        }

        while (!numbers.isEmpty()) {
            if (answer > 0) {
                break;
            }

            boolean check = true;
            for (int j = 2; j <= Math.sqrt(numbers.get(0)); j++) {
                if (numbers.get(0) % j == 0) {
                    check = false;
                    break;
                }
            }

            if (check) {
                P = numbers.get(0);

                for (int num = 0; num < numbers.size(); num++) {
                    if (numbers.get(num) % P == 0) {
                        count++;
                        if (count == K) {
                            answer = numbers.get(num);
                            break;
                        }
                        numbers.remove(num);
                    }
                }
            }
        }

        sb.append(answer).append('\n');


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