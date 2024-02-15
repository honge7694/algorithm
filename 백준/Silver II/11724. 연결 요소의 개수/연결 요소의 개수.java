import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int u, v, N, M;
    static boolean[][] graph;
    static boolean[] visited;

    static void dfs(int idx) {
        if (visited[idx] == true) {
            return;
        } else {
            visited[idx] = true;
            for (int i = 1; i < N+1; i++) {
                if (graph[idx][i] == true) { // 간선 연결이 되어있다면
                    dfs(i);
                }
            }
        }
    }

    static void input() throws Exception {
        N = scan.nextInt();
        M = scan.nextInt();

        graph= new boolean[N+1][N+1];
        visited = new boolean[N+1];

        for (int i = 0; i < M; i++) {
            u = scan.nextInt();
            v = scan.nextInt();

            graph[u][v] = true;
            graph[v][u] = true;
        }

        int count = 0;
        for (int i = 1; i < N+1; i++) {
            if (visited[i] == false) {
                dfs(i);
                count++;
            }
        }

        sb.append(count).append("\n");

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