import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    static void input() throws Exception {
        /** 메모리 초과
        int N = scan.nextInt();
        int[] A = new int[N];
        for(int i = 0; i < N; i++) {
            A[i] = scan.nextInt();
        }
        Arrays.parallelSort(A); // 배열의 길이가 큰 경우 사용

        int M = scan.nextInt();
        int[] numbers = new int[M];
        for(int i = 0; i < M; i++) {
            numbers[i] = scan.nextInt();
        }

        int[] answer = new int[M];
        int medianNum = N / 2;

        for (int i = 0; i < M; i++) {
            if (numbers[i] < medianNum) {
                int[] smallNumbers = Arrays.copyOfRange(A, 0, medianNum);
                for (int j = 0; j < medianNum; j++) {
                    if (numbers[i] == smallNumbers[j]) {
                        answer[i] = 1;
                        break;
                    }
                }
            } else if (numbers[i] >= medianNum){
                int[] bigNumbers = Arrays.copyOfRange(A, medianNum, N);
                for (int j = 0; j < bigNumbers.length; j++) {
                    if (numbers[i] == bigNumbers[j]) {
                        answer[i] = 1;
                        break;
                    }
                }
            }
        }

        for(int ans : answer) {
            sb.append(ans).append('\n');
        }
        */
        int N = scan.nextInt();
        HashMap<Integer, Integer> A = new HashMap<>();
        for(int i = 0; i < N; i++) {
            A.put(scan.nextInt(), 0);
        }

        int M = scan.nextInt();
        int[] numbers = new int[M];
        for(int i = 0; i < M; i++) {
            numbers[i] = scan.nextInt();
        }

        int[] answer = new int[M];
        for (int i = 0; i < M; i++) {
            if (A.containsKey(numbers[i])) {
                answer[i] = 1;
            }
        }

        for(int ans : answer) {
            sb.append(ans).append('\n');
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