menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair 

=>'''

saldo = 0
limite = 500
numero_saques = 0
LIMITE=SAQUES = 3
extrato = ""

while True:
   escolha = input(menu)

   if escolha == "d":
    valor = float(input("Informe o valor do depósito: "))
    
    
    if valor > 0:
     saldo += valor
     extrato += f"Déposito de R$ {valor:.2f}\n"
     
    else:
       print("Operação cancelada! O valor informado é inválido")

