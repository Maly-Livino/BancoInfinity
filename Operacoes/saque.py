from banco import banco, obterConta

def sacar(conta:int, valor:float) -> None:
    cliente = obterConta(conta)
    if cliente:
        if cliente['saldo'] >= valor:
            cliente['saldo'] -= valor
            print("--Saque Realizado com Sucesso---")
        else:
            print("Saldo Insuficiente")
    else:
        print("Cliente não encontrado")

sacar(1,500)
print(banco)