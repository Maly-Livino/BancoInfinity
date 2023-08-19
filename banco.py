from typing import Optional
from time import sleep

banco = [
    {"conta": 1, "cliente": "Luis", "saldo": 1000.0},
    {"conta": 2, "cliente": "Mariana", "saldo": 2500.0}
]

conta_atual = 2

def adicionarConta(cliente: str, saldo: float) -> None:
    global conta_atual
    conta_atual += 1
    conta = {
        "conta": conta_atual,
        "cliente": cliente,
        "saldo": saldo
    }
    banco.append(conta)
    print("--Conta Cadastrada com Sucesso--")

def obterConta(conta:int) -> Optional[dict or None]:
    for cliente in banco:
        if cliente["conta"] == conta:
            return cliente
        return None

def deletarConta(conta:int) -> None:
    cliente = obterConta(conta)
    if cliente:
        banco.remove(cliente)
        print("-- Cliente Removido com Sucesso--")
    else:
        print("--Cliente não Encontrado--")

def listarContas() -> None:
    for cliente in banco:
        print("---Dados do Cliente---")
        print(f"N. Conta:{cliente['conta']}")
        print(f"Saldo:{cliente['saldo']}")
        print("----------------------------------------")
        sleep(2)
def atualizarNome(conta:int , novo_nome:str) -> None:
    cliente = obterConta(conta)
    if cliente:
        cliente["cliente"] = novo_nome
        print("---Dados Alterados com Sucesso---")
    else:
        print("Cliente não Encontrado")

def atualizarSaldo(conta: int, novo_saldo: float) -> None:
    cliente = obterConta(conta)
    if cliente:
        cliente['saldo'] = novo_saldo
        print('Dados alterados com sucesso!')
    else:
        print('Cliente não encontrado!')



adicionarConta("Carlos",500)
print(obterConta(2))
deletarConta(2)
print(banco)
atualizarNome(1, "João")
atualizarSaldo(1, 4000)
listarContas()

