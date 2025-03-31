package ar.edu.itba.ss;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class RepeatedIsing {
    public static void main(String[] args){
        double[] p_values = {0.2, 0.15, 0.125, 0.1125, 0.10625, 0.05, 0.075, 0.0875, 0.09375, 0.096875, 0.01};
        int seed = Integer.parseInt(System.getProperty("seed"));

        for(double p: p_values){
            Random random = new Random(seed);

            IsingMethod method = new IsingMethod(50, p, 30000, random);
            try (FileWriter fb = new FileWriter(String.format("p_%.6f_s_%d", p, seed))) {
                method.execute(fb);
            } catch (IOException e) {
                throw new RuntimeException(e.getMessage());
            }
        }
    }
}
