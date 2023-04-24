public class Main {
    public static void main(String[] args) {
        Calculadora calc = new Calculadora();
        System.out.println(calc.Somar(1,1));
        System.out.println(calc.Somar(new int[]{1, 2, 3}));
    }
}