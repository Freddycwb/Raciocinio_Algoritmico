public class Pessoa {
    private Conta conta;

    public void Depositar(float valor) {
        conta.Depositar(valor);
    }

    public Conta getConta() {
        return conta;
    }

    public Pessoa(Conta conta) {
        this.conta = conta;
    }
}
