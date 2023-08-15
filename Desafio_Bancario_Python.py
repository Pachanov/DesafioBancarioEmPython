menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("informa o valor do deposito "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            
        else:
            print("Operaçao falhou o valor informado é invalido")
            
    elif opcao == "s":
            valor = float(input("informa o valor do Saque"))
            
            excedeu_saldo = valor > saldo
            
            excedeu_limite = valor > limite
            
            excedeu_saques = numero_saques> LIMITE_SAQUES
            
            if excedeu_saldo:
                print("Operaçao falhou!Voce nao tem saldo suficiente.")
            
            elif excedeu_limite:
                print("Operaçao falhou!Valor do saque excede o limite.")
        
            elif excedeu_saques:
                print("Operaçao falhou!Numero de saques excedido.")
        
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R${valor:.2f}\n"
                numero_saques += 1
            
            else:
                print("Operacao falhou o valor informado é invalido")
                
    elif opcao == "e":
        print("\n==================EXTRATO====================")
        print("Nao foram realizados movimentaçoes." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("\n==================+++++++====================")
        
    elif opcao == "q":
        break
    
    else:
        print("Operacao invalida, por favor selecione novamente a operaçao desejada")