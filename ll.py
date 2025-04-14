rendaAnual = float(input("Digite a sua renda anual"))
credito = int(input("Digite o credito do cliente: "))
dividasPendentes = int(input("Digite a quantidade de dividas pendentes: "))

if rendaAnual >= 60000 and credito >= 720 and dividasPendentes == 0:
    print("Taxa de juros baixa !")
elif rendaAnual >= 40000 and credito >= 680 and dividasPendentes <= 1:
    print("Taxa de juros moderada !")
elif rendaAnual >= 30000 and credito >= 650 and dividasPendentes <=2:
    print("Taxa de juros alta !")
else:
    print("Não atende nenhum dos critérios !")

