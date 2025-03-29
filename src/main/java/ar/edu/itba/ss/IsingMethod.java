package ar.edu.itba.ss;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class IsingMethod {

    private final int[][] grid;
    private final Random random;
    private final long maxSteps;
    private final int N;
    private final double p;

    public IsingMethod(int N, double p, long maxSteps, Random random) {
        this.N = N;
        this.p = p;
        this.maxSteps = maxSteps;
        this.random = random;
        grid = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                grid[i][j] = random.nextBoolean() ? 1 : -1;
            }
        }
    }

    public static void main(String[] args) {
        if (System.getProperty("n") == null || System.getProperty("p") == null) {
            System.err.println("Missing required parameters");
            System.exit(1);
        }
        int N = Integer.parseInt(System.getProperty("n"));
        double p = Double.parseDouble(System.getProperty("p"));

        Random random = new Random();
        if (System.getProperty("seed") != null) {
            random.setSeed(Integer.parseInt(System.getProperty("seed")));
        }

        long mcSteps = 100;
        if (System.getProperty("mcSteps") != null) {
            mcSteps = Long.parseLong(System.getProperty("mcSteps"));
        }

        String outputFileName = "output.txt";
        if (System.getProperty("output") != null){
            outputFileName = System.getProperty("output");
        }

        IsingMethod method = new IsingMethod(N, p, mcSteps, random);
        try (FileWriter fb = new FileWriter("output.txt")) {
            method.execute(fb);
        } catch (IOException e) {
            throw new RuntimeException(e.getMessage());
        }
    }


    public void execute(FileWriter fb) throws IOException {
        fb.write(String.format("N: %d\n", N));
        fb.write(String.format("p: %.2f\n\n", p));

        for (long monteCarloStep = 0; monteCarloStep < maxSteps; monteCarloStep++) {
            for (int i = 0; i < N * N; i++) {

                int randomPersonRow = random.nextInt(0, N);
                int randomPersonCol = random.nextInt(0, N);

                int majorityOpinion = getNeighbourOpinions(randomPersonRow, randomPersonCol);
                if (majorityOpinion == 0) {
                    majorityOpinion = grid[randomPersonRow][randomPersonCol];
                }

                if (random.nextDouble() < p) {
                    grid[randomPersonRow][randomPersonCol] = -grid[randomPersonRow][randomPersonCol];
                } else {
                    grid[randomPersonRow][randomPersonCol] = majorityOpinion;
                }
            }
            writeMonteCarloStepCount(monteCarloStep, fb);
        }

    }

    public int getNeighbourOpinions(int row, int col) {
        int opinionDown = grid[row > 0? row-1: N-1][col];
        int opinionUp = grid[(row+1)%N][col];
        int opinionLeft = grid[row][col > 0? col-1: N-1];
        int opinionRight = grid[row][(col+1)%N];

        return (int) Math.signum((double)(opinionUp + opinionDown + opinionLeft + opinionRight));
    }

    private String gridToString(int[][] grid, int N){
        StringBuilder sb = new StringBuilder("[\n");
        for (int i = 0; i < N; i++){
            sb.append("[ ");
            for (int j = 0; j < N; j++){
                sb.append(grid[i][j]).append(' ');
            }
            sb.append("]\n");
        }
        sb.append("]\n");
        return sb.toString();
    }

    public void writeMonteCarloStepCount(long step, FileWriter fb) throws IOException {
        //fb.append(String.valueOf(step));
        //fb.append('\n');
        fb.append(gridToString(grid, N));
        if (step == maxSteps){
            fb.append("end");
        } else {
            fb.append("next\n");
        }
    }
}