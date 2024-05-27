menu = '''

Olá! O que você deseja fazer hoje?

[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair 

=>'''

saldo = 0
limitevalorsaque = 500
numero_saques_realizados = 0
limite_saques_por_dia = 3
extrato = ""

while True:
    escolha = input(menu)

    if escolha == "x":
        print("Obrigada por escolher o nosso banco. Até logo!")
        break
    
    if escolha == "d":
        valor= float(input("Digite o valor para depósito: "))
        
        if valor > 0:
            print("Depósito realizado com sucesso!")
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"
        else:
            print("Operação cancelada! Informe um valor válido.")
            
    if escolha == "s":
        valor = float(input("Digite o valor para saque: "))
        passou_limite_saque = valor > limitevalorsaque
        passou_saldo = valor > saldo
        passou_limite_diario = numero_saques_realizados >= limite_saques_por_dia
    
        if passou_limite_saque:
            print("Operação cancelada! O valor informado ultrapassa o limite.")
        elif passou_saldo:
            print("Operação cancelada! O valor informado ultrapassa o saldo em conta.")
        elif passou_limite_diario:
            print("Operação cancelada! Você já realizou todos os saques permitidos hoje.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de R${valor:.2f}\n"
            numero_saques_realizados += 1 
        else:
            print("Operação cancelada! Tente novamente.")
            
    if escolha == "e":
        print("\n========== EXTRATO ==========")
        print("Nenhuma movimentação realizada na conta" if not extrato else extrato) 
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================")
        
    
            
            
            