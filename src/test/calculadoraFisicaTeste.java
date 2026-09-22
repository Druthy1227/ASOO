package test;

import main.calculadoraFisica;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class calculadoraFisicaTeste {

    @Test
    public void testEnergiaPotencial() {
        double massa = 10.0;
        double altura = 5.0;
        double resultadoEsperado = 490.5;

        double resultadoObtido = calculadoraFisica.energiaPotencial(massa, altura);

        System.out.println("O resultado obtido foi:" + resultadoObtido);

        assertEquals(resultadoObtido, resultadoObtido, 0.001);
    }

}

