import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        while(T-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int r1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            int r2 = Integer.parseInt(st.nextToken());

            int distance = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
            int rSumSquared = (r1 + r2) * (r1 + r2);
            int rDiffSquared = (r1 - r2) * (r1 - r2);
            if(rDiffSquared < distance && distance < rSumSquared) {
                sb.append(2);
            } else if (x1 == x2 && y1 == y2 && r1 == r2) {
                sb.append(-1);
            } else if (distance == rDiffSquared || distance == rSumSquared) {
                sb.append(1);
            } else {
                sb.append(0);
            }
            System.out.println(sb);
            sb.setLength(0);
        }
        br.close();
    }
}
