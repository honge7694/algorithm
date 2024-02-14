import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    static int N, M, K;
    static boolean[][] graph;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};

    static void bfs(int x, int y) {
        LinkedList<Integer[]> deque = new LinkedList<>();
        deque.addFirst(new Integer[]{x, y});

        while(!deque.isEmpty()) {
            Integer[] loc = deque.removeFirst();
            int locX = loc[0];
            int locY = loc[1];

            for (int i = 0; i < 4; i++) {
                int vx = locX + dx[i];
                int vy = locY + dy[i];

                if (vx >= N || vx < 0 || vy >= M || vy < 0) {
                    continue;
                }

                if (graph[vx][vy] == true) {
                    graph[vx][vy] = false;
                    deque.addFirst(new Integer[]{vx, vy});
                }
            }
        }
    }
    static void input() throws Exception {
        int T = scan.nextInt();

        for (int i = 0; i < T; i++) {
            M = scan.nextInt();
            N = scan.nextInt();
            K = scan.nextInt(); // 배추 위치

            // 그래프
            graph = new boolean[N][M];

            // 배추 위치 심기
            for (int j = 0; j < K; j++) {
                int x = scan.nextInt();
                int y = scan.nextInt();

                graph[y][x] = true;
            }

            // 배추 카운트
            int count = 0;
            for (int x = 0; x < N; x++) {
                for (int y = 0; y < M; y++) {
                    if (graph[x][y] == true) {
                        bfs(x, y);
                        count++;
                    }
                }
            }
            sb.append(count).append("\n");
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