# -*- coding: utf-8 -*-
"""Sistema_bancario.ipynb
"""

menu  = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo   = 0
limite  = 500
extrato = ""
n_saque = 0
LIMITE_SAQUE = 3

while True:
  opçao = input(menu)

  if opçao    == "d":
    print("Digite o valor do deposito:")
    dep = float(input())
    saldo += dep
    extrato += f"\nDeposito: R$ {dep}"
    print(f"Deposito realizado!")

  elif opçao == "s":
    print("Digite o valor do saque:")
    saq = float(input())
    if saq <=500:
      if saq > saldo :      print(f"Saldo insuficiente!")
      elif saq<= saldo and n_saque <3 :
        saldo -= saq
        extrato += f"\nSaque: R$ {saq}"
        print(f"Saque realizado!")
        n_saque += 1
      else:   print(f"Excedeu o numero limite de saque diario, tente novamente outro dia.")
    else:   print(f"Excedeu o valor limite de saque diario, tente novamente outro dia.")

  elif opçao  == "e":
    print("Extrato:",extrato)
    print(f"Saldo: {saldo}")

  elif opçao  == "q":
    break
  else:
    print("Opção invalida, tente novamente.")