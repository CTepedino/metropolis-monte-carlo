package ar.edu.itba.ss;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Locale;
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
        try (FileWriter fb = new FileWriter(outputFileName)) {
            method.execute(fb);
        } catch (IOException e) {
            throw new RuntimeException(e.getMessage());
        }
    }


    public void execute(FileWriter fb) throws IOException {
        fb.write(String.format("%d\n", N));
        fb.write(String.format(Locale.US,"%.6f\n", p));
        fb.write(String.format("%d\n", maxSteps));

        fb.write(gridToString());

        for (long monteCarloStep = 0; monteCarloStep < maxSteps; monteCarloStep++) {
            int[][] previousGrid = new int[N][N];
            for (int i = 0; i < N; i++) {
                System.arraycopy(grid[i], 0, previousGrid[i], 0, N);
            }

            for (int i = 0; i < N * N; i++) {
                int randomPersonRow = random.nextInt(0, N);
                int randomPersonCol = random.nextInt(0, N);

                if (random.nextDouble() < p) {
                    grid[randomPersonRow][randomPersonCol] = -grid[randomPersonRow][randomPersonCol];
                } else {
                    int majorityOpinion = getNeighbourOpinions(randomPersonRow, randomPersonCol);
                    if (majorityOpinion == 0) {
                        majorityOpinion = grid[randomPersonRow][randomPersonCol];
                    }
                    grid[randomPersonRow][randomPersonCol] = majorityOpinion;
                }
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (previousGrid[i][j] != grid[i][j]) {
                        fb.write(String.format("%d %d\n", i, j));
                    }
                }
            }

            if (monteCarloStep != maxSteps - 1) {
                fb.write("next\n");
            } else {
                fb.write("end");
            }
        }
    }

    public int getNeighbourOpinions(int row, int col) {
        int opinionUp = grid[row > 0? row-1: N-1][col];
        int opinionDown = grid[(row+1)%N][col];
        int opinionLeft = grid[row][col > 0? col-1: N-1];
        int opinionRight = grid[row][(col+1)%N];

        return (int) Math.signum((double)(opinionUp + opinionDown + opinionLeft + opinionRight));
    }

    private String gridToString(){
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++){
            for (int j = 0; j < N; j++){
                sb.append(grid[i][j]).append(' ');
            }
            sb.append('\n');
        }
        return sb.toString();
    }

}