package org.example;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
import java.util.function.Predicate;

public class MetropolisMethod {

    public static void main(String[] args){
        if (System.getProperty("n") == null || System.getProperty("p") == null){
            System.err.println("Missing required parameters");
            System.exit(1);
        }
        int N = Integer.parseInt(System.getProperty("n"));
        double p = Double.parseDouble(System.getProperty("p"));

        Random random = new Random();
        if (System.getProperty("seed") != null){
            random.setSeed(Integer.parseInt(System.getProperty("seed")));
        }

        int[][] grid = new int[N][N];
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                grid[i][j] = random.nextBoolean()? 1: -1;
            }
        }

        Predicate<Long> cutCondition;
        if (System.getProperty("iterations") != null){
            long iterations = Long.parseLong(System.getProperty("iterations"));
            cutCondition = (n) ->  n < iterations;
        } else {
            cutCondition = (n) -> true;
        }
        double[] Ms = new double[N];

        try(FileWriter fb = new FileWriter("output.txt")){
            for(long it = 0; cutCondition.test(it); it++){
                int randomPersonRow = random.nextInt(0, N);
                int randomPersonCol = random.nextInt(0, N);

                int mayorityOpinion = getNeighbourOpinions(randomPersonCol, randomPersonRow, N, grid);
                if (mayorityOpinion == 0){
                    mayorityOpinion = grid[randomPersonRow][randomPersonCol];
                }
                int coinFlip = random.nextInt(0, 101);
                if (coinFlip < p*100){
                    grid[randomPersonRow][randomPersonCol] = - grid[randomPersonRow][randomPersonCol];
                } else {
                    grid[randomPersonRow][randomPersonCol] = mayorityOpinion;
                }
                double consensus = getConsensus(N, grid);
                if (it % Math.pow(N, 2) == 0){
                    writeOutput(grid, N, consensus, !cutCondition.test(it+1), fb);
                }
            }
        } catch (IOException e){
            throw new RuntimeException(e.getMessage());
        }

        // double susceptibility = getSusceptibility(N, Mestationaries);

    }

    public static int getNeighbourOpinions(int col, int row, int N, int[][] grid){
        int opinionDown = grid[row > 0? row-1: N-1][col];
        int opinionUp = grid[(row+1)%N][col];
        int opinionLeft = grid[row][col > 0? col-1: N-1];
        int opinionRight = grid[row][(col+1)%N];

        return (int) Math.signum((double)(opinionUp + opinionDown + opinionLeft + opinionRight));
    }

    public static double getConsensus(int N, int[][] grid){
        int sum = 0;
        for (int i = 0; i < N; i++){
            for (int j = 0; j < N; j++){
                sum += grid[i][j];
            }
        }
        return Math.abs(sum/(Math.pow(N, 2.0)));
    }

    public static double getSusceptibility(int N, double[] estacionaryM){
        int medianM = 0;
        int medianSquaredM = 0;
        for (int i = 0; i < estacionaryM.length; i++){
            medianM += estacionaryM[i];
            medianSquaredM += Math.pow(estacionaryM[i], 2.0);
        }
        medianSquaredM /= estacionaryM.length;
        medianM /= estacionaryM.length;
        return Math.pow(N, 2.0) * (medianSquaredM - Math.pow(medianM, 2.0));
    }

    public static String gridToString(int[][] grid, int N){
        StringBuilder sb = new StringBuilder("[\n");
        for (int i = 0; i < N; i++){
            sb.append("[ ");
            for (int j = 0; j < N; j++){
                sb.append(grid[i][j]).append(' ');
            }
            sb.append(" ]\n");
        }
        sb.append("]\n");
        return sb.toString();
    }

    public static void writeOutput(int[][] grid, int N, double M, boolean last, FileWriter fb) throws IOException{
        fb.append(gridToString(grid, N));
        fb.append(String.valueOf(M));
        if (last){
            fb.append("end");
        } else {
            fb.append("next\n");
        }
    }
}