public class Main {
    public static void main(String[] args) {
        Pessoa pessoa1 = new Pessoa(new ContaCorrente(5000));
        Pessoa pessoa2 = new Pessoa(new ContaPoupanca(10000));

        System.out.println("Saldo pessoa 1: ");
        pessoa1.getConta().MostrarSaldo();
        System.out.println("Saldo pessoa 2: ");
        pessoa2.getConta().MostrarSaldo();

        pessoa1.Depositar(5000);
        System.out.println("Saldo pessoa 1 após depositar: ");
        pessoa1.getConta().MostrarSaldo();
    }
}