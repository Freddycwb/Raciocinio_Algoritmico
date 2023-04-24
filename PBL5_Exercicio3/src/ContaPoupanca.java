public class ContaPoupanca extends Conta {
    @Override
    public void MostrarSaldo() {
        System.out.println(String.format("O valor do saldo é: R$%.2f", getSaldo()*1.005f));
    }

    public ContaPoupanca(float valor) {
        super(valor);
    }
}
