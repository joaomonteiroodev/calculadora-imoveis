# Calculadora de Financiamento Imobiliário
# Sistema: Tabela Price

def calcular():
    print()
    print("=== Calculadora de Financiamento ===")
    print()

    valor_imovel = float(input("Valor do imóvel (R$): "))

    while True:
        entrada = float(input("Valor da entrada (R$): "))
        if entrada < valor_imovel:
            break
        print("⚠ A entrada não pode ser maior ou igual ao valor do imóvel. Tente novamente.")

    taxa_juros = float(input("Taxa de juros mensal (%): "))
    prazo_meses = int(input("Prazo em meses: "))

    valor_financiado = valor_imovel - entrada
    taxa = taxa_juros / 100

    parcela = valor_financiado * (taxa * (1 + taxa) ** prazo_meses) / ((1 + taxa) ** prazo_meses - 1)

    total_pago = parcela * prazo_meses
    total_juros = total_pago - valor_financiado

    print()
    print("=== Resultado ===")
    print(f"Valor financiado: R$ {valor_financiado:,.2f}")
    print(f"Parcela mensal:   R$ {parcela:,.2f}")
    print(f"Total pago:       R$ {total_pago:,.2f}")
    print(f"Total em juros:   R$ {total_juros:,.2f}")
    print()

# Loop principal
while True:
    calcular()
    resposta = input("Calcular novamente? (s/n): ").strip().lower()
    if resposta != "s":
        print()
        print("Encerrando. Até logo!")
        break