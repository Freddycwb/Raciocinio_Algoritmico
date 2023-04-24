public class Conta {
    private float saldo;

    protected float getSaldo() {
        return saldo;
    }

    public void Depositar(float valor) {
        saldo += valor;
    }

    public void MostrarSaldo() {
        System.out.println(String.format("O valor do saldo é: R$%.2f", saldo));
    }

    public Conta(float saldo) {
        this.saldo = saldo;
    }
}
