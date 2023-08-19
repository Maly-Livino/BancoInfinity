from banco import obterConta
def transferir(contaOri: int, contaDes: int, valor:float) -> None:
     contaOrigem = obterConta(contaOri)
     contaDestino = obterConta(contaDes)
     if contaOrigem and contaDestino:
         if contaOrigem['saldo'] >= valor:
             contaDestino['saldo'] += valor
             contaOrigem['saldo'] -= valor
             print("---Transferencia Realizada com Sucesso---")
         else:
             print("Saldo Insuficiente para a Transferencia")
     else:
         print("---Uma das contas não existe---")