from ..banco import obterConta, banco

def consultarSaldo(conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        print(f"Seu Saldo:{cliente['saldp']}")
    else:
        print('Cliente não encontrado')