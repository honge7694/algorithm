import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static void input() throws Exception {
        int T = scan.nextInt();
        for(int count = 0; count < T; count++) {
            int N = scan.nextInt();
            int[] note1 = new int[N];
            for (int i = 0; i < N; i++) {
                note1[i] = scan.nextInt();
            }

            Arrays.sort(note1);

            int M = scan.nextInt();
            int[] note2 = new int[M];
            for (int i = 0; i < M; i++) {
                note2[i] = scan.nextInt();
            }

            for (int note : note2) {
                int start = 0, end = N - 1;
                boolean isExist = false;

                while (start <= end) {
                    int mid = (start + end) / 2;
                    if (note1[mid] == note) {
                        sb.append(1).append('\n');
                        isExist = true;
                        break;
                    } else if (note1[mid] >= note) {
                        end = mid - 1;
                    } else {
                        start = mid + 1;
                    }
                }

                if(!isExist) {
                    sb.append(0).append('\n');
                }
            }
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