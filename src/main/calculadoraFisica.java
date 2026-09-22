package main;

public class calculadoraFisica {

    public static final double CONSTANTE_GRAVITACIONAL = 9.81;

    public static double energiaPotencial (double massa, double altura) {
        return massa * CONSTANTE_GRAVITACIONAL * altura;
    }
}
