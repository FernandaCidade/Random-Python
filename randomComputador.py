import random

continuar = 1
while continuar:
    print("Número aleatório gerado: ", random.randint(1,6))
    continuar = int(input("Gerar novamente?\n1.Sim\n0.Não\n"))
