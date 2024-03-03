import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    static void input() throws Exception {
        int N = scan.nextInt();
        ArrayList<Integer> km = new ArrayList<>();
        ArrayList<Integer> oil = new ArrayList<>();
        int currentOil = 0, cost = 0, cheapOil = 0, distance = 0;

        for(int i = 0; i < N-1; i++) {
            km.add(scan.nextInt());
        }

        for(int i = 0; i < N; i++) {
            oil.add(scan.nextInt());
        }

        // 0. 총 거리를 구한다.
        // 1. oil이 가장 싼 곳을 찾는다.(맨 마지막 마을의 oil은 무시)
        // 2-1. 처음에 있다면 => 총 거리만큼 기름 넣기
        // 2-2. 중간에 있다면 => 거리만큼까지만 oil 채우기

        // 총 거리 구하기
        for(int i = 0; i < N-1; i++) {
            distance += km.get(i);
//            System.out.println("distance = " + distance);
        }

        // 가장 싼 기름 구하기
        for(int i = 0; i < N-2; i++) {
            if (oil.get(i) > oil.get(i+1)) {
                cheapOil = oil.get(i+1);
            }
        }

        for (int i = 0; i < N-1; i++) {
            if (cheapOil == oil.get(i)) {
                while(currentOil < distance) {
                    cost += oil.get(i);
                    currentOil += 1;
//                    System.out.println("i2 : " + i + " currentOil = " + currentOil + " cost  = " + cost);
                }
            } else if(currentOil < km.get(i)-1) {
                while(currentOil < km.get(i)) {
                    cost += oil.get(i);
                    currentOil += 1;
//                    System.out.println("i1 : " + i + " currentOil = " + currentOil + " cost  = " + cost);
                }
            }

            // 다음 마을로 이동
            currentOil -= km.get(i);
            distance -= km.get(i);
//            System.out.println("distance = " + distance);
        }

        sb.append(cost);
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