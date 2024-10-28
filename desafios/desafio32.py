class SaldoInsuficienteException(Exception):
    def __init__(self, mensagem="Saldo insuficiente para realizar o saque."):
        super().__init__(mensagem)


class Conta:
    def __init__(self):
        self.__saldo = 0.0  # Atributo privado para o saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return f"Depósito de R${valor:.2f} realizado com sucesso."
        return "Valor de depósito inválido."

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
                return f"Retirada de R${valor:.2f} efetuada com sucesso."
            else:
                raise SaldoInsuficienteException()  # Lança a exceção se o saldo for insuficiente
        return "Valor de saque inválido."

    def exibir_saldo(self):
        return f"Seu saldo é de R${self.__saldo:.2f}."
    
# Testando a exceção personalizada
minha_conta = Conta()
print(minha_conta.depositar(500))  # Depósito de R$500.00 realizado com sucesso.

try:
    print(minha_conta.sacar(600))  # Tenta sacar R$600.00, mas gera exceção
except SaldoInsuficienteException as e:
    print(e)  # Saída: Saldo insuficiente para realizar o saque.
    
print(minha_conta.exibir_saldo())  # Saída: Seu saldo é de R$500.00.

            
        