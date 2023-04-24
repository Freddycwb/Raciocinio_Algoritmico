public class Calculadora {
    public int Somar(int a, int b) {
        return a + b;
    }

    public int Somar(int[] valores) {
        int resultado = 0;
        for(int valor : valores) {
            resultado += valor;
        }
        return resultado;
    }

    public int Subtrair(int a, int b) {
        return a - b;
    }

    public int Subtrair(int[] valores) {
        int maior = valores[0];
        int maiorIndice = 0;
        for (int i = 1; i < valores.length; i++) {
            if (valores[i] > maior) {
                maior = valores[i];
                maiorIndice = i;
            }
        }
        valores[maiorIndice] = 0;

        for (int valor : valores) {
            maior -= valor;
        }

        return maior;
    }

    public int Multiplicar(int a, int b) {
        return a * b;
    }

    public int[] Multiplicar(int[] valores, int multiplicador) {
        int[] resultado = valores;
        for (int i = 0; i < valores.length; i++) {
            resultado[i] *= multiplicador;
        }
        return resultado;
    }

    public int Dividir(int a, int b) {
        if (b != 0) {
            return a/b;
        }
        return 0;
    }

    public int Dividir(int[] valores) {
        int divisor = 0;
        int dividendo = 0;

        for(int i = 0; i < valores.length; i++) {
            if (i % 2 == 0) {
                divisor += valores[i];
            }
            else {
                dividendo += valores[i];
            }
        }

        if (divisor != 0) {
            return dividendo/divisor;
        }
        return 0;
    }
}
