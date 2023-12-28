# -*- coding: utf-8 -*-
""" 
    Sistema_bancario v2
    Nessa versão sera utilizado o conhecimento de funções
"""

menu  = """
[a] Cadastrar usuario.
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
def User():
    global user
    user_ = input('Por favor, digite seu nome:')
    cpf_ = input('Digite seu CPF:')
    if cpf_ in user.keys():
        print("Usuaria já está cadastrado!")
    else:
        logradoro_  = input('Logradouro:')
        nro_        = input('N° da casa:')
        bairro_     = input('Bairro:')
        cidade_     = input('Cidade:')
        user[f"{cpf_}"] =  {'Dados Pessoas': {'Name':user_,'logradoro':logradoro_,'nro': nro_,'bairro': bairro_,'cidade/sigla estado': cidade_} }
        print("Usuaria cadastrado com sucesso!")
        Bank_Account(cpf_)
    
def Bank_Account(cpf_):  
    global user

    bank_account_                   = input('Digite sua conta bancaria:')
    user[f"{cpf_}"]['Bank account'] = bank_account_
    user[f"{cpf_}"]['Saldo']        = 0
    user[f"{cpf_}"]['Extrato']      = ""
    user[f"{cpf_}"]['n_saque']      = 0

def Deposit():
    global user
    
    cpf_ = input('Digite seu CPF:')
    if cpf_ in user.keys():
        saldo_   = user[f"{cpf_}"]["Saldo"]
        extrato_ = user[f"{cpf_}"]["Extrato"]
        
        print("Digite o valor do deposito:")
        dep_     = float(input())
        saldo_  += dep_
        extrato_+= f"\n Deposito: R$ {dep_}"
        
        user[f"{cpf_}"]["Saldo"]   = saldo_
        user[f"{cpf_}"]["Extrato"] = extrato_
        
        print(f"Deposito realizado!")

def Withdaw():
    global user
    
    cpf_ = input('Digite seu CPF:')
    if cpf_ in user.keys():
        saldo_   = user[f"{cpf_}"]["Saldo"]
        extrato_ = user[f"{cpf_}"]["Extrato"]
        n_saque_ = user[f"{cpf_}"]["n_saque"]
          
        print("Digite o valor do saque:")
        saq_ = float(input())
        
        if saq_ <=500:     
            if saq_ > saldo_ :      
                print(f"Saldo insuficiente!")
                
            elif saq_ <= saldo_ and n_saque_ < 3 :
                saldo_   -= saq_
                extrato_ += f"\n Saque: R$ {saq_}"
                n_saque_ += 1
                print(f"Saque realizado!")
                
                user[f"{cpf_}"]["Saldo"]   = saldo_
                user[f"{cpf_}"]["Extrato"] = extrato_
                user[f"{cpf_}"]["n_saque"] = n_saque_
                
            else:   print(f"Excedeu o número limite de saque diario, tente novamente outro dia.")
            
        else:   print(f"Excedeu o valor limite de saque diario, tente novamente outro dia.")

def Extract():
    global user
    
    cpf_ = input('Digite seu CPF:')
    if cpf_ in user.keys():
        print("Olá Sr./Sra. ",user[f"{cpf_}"]["Dados Pessoas"]['Name'])
        print("Extrato:",user[f"{cpf_}"]["Extrato"])
        print("Saldo:",  user[f"{cpf_}"]["Saldo"])

user = {}
limite  = 500
LIMITE_SAQUE = 3

while True:
  opçao = input(menu)
  if   opçao == "d": Deposit()
  elif opçao == "s": Withdaw()
  elif opçao == "e": Extract()
  elif opçao == "a": User()
  elif opçao == "q": break
  else:              print("Opção invalida, tente novamente.")