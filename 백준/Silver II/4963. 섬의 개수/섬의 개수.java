import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    static int w, h;
    static int[][] graph;
    static int[] dx = {0, 0, -1, 1, -1, -1, 1, 1}; // 상 하 좌 우, 좌상, 좌하, 우상, 우하
    static int[] dy = {-1, 1, 0, 0, -1, 1, -1, 1};

    static void bfs(int y, int x) {
        LinkedList<Integer[]> deque = new LinkedList<>();
        deque.addFirst((new Integer[]{y, x}));

        while(!deque.isEmpty()) {
            Integer[] loc = deque.removeFirst();
            int locY = loc[0];
            int locX = loc[1];

            for (int i = 0; i < 8; i++) {
                int my = locY + dy[i];
                int mx = locX + dx[i];

                if (mx >= w || my >= h || mx < 0 || my < 0) {
                    continue;
                }

                if (graph[my][mx] == 1) {
                    graph[my][mx] = 0;
                    deque.add(new Integer[]{my, mx});
                }
            }
        }
    }

    static void input() throws Exception {
        while (true) {
            w = scan.nextInt();
            h = scan.nextInt();

            if (w == 0 && h == 0) {
                break;
            }

            graph = new int[h][w];
            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    graph[i][j] = scan.nextInt();
                }
            }

            int count = 0;
            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    if (graph[i][j] == 1) {
                        bfs(i, j);
                        count++;
                    }
                }
            }

            sb.append(count).append('\n');
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