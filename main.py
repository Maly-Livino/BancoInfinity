from banco import *
from Operacoes.deposito import depositar
from Operacoes.consulta import consultarSaldo
from Operacoes.saque import sacar
from Operacoes.transferencia import transferir

def menu():
    while True:
        print("--- Sistema Bancario---")
        print('1 - Adicionar Conta')
        print("2 - Editar Conta")
        print("3 - COnsultar Conta")
        print("4 - Apagar Conta")
        print("5 - Listar Cntas")
        print("6 - Atualizar Nome")
        print("7 - Atualizar Saldo")
        print("8 - Realizar Saque")
        print("9 - Realizar Deposito")
        print("10 - Consultar Saldo")
        print("11 - Transferencia ")
        print("12 - Sair")
        opcao = input("Selecione uma Opção:")