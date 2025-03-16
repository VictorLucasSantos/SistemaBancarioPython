from datetime import datetime

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def valida_valores(valor: float):
    """Valida se o valor é numérico e positivo"""
    if not isinstance(valor, (int, float)):
        raise ValueError("Informe valores numéricos válidos.")

    if valor <= 0:
        raise ValueError("Informe um valor positivo")

    return valor


while True:
    opcao = input(menu).strip().lower()

    match opcao:
        case "d":
            try:
                valor_deposito = valida_valores(
                    float(input("Informe o valor a ser depositado: "))
                )
            except ValueError as e:
                print(f"Erro: {e}")
                continue

            saldo += valor_deposito
            extrato += f"Depósito de R$ {valor_deposito:.2f} às {datetime.now().strftime('%Y-%m-%d %H:%M')} horas.\n"
            print(
                f"Depósito realizado com sucesso às {datetime.now().strftime('%Y-%m-%d %H:%M')} horas!"
            )

        case "s":
            if saldo == 0:
                print("O saldo da conta está zerado!")
                continue

            if numero_saques >= LIMITE_SAQUES:
                print("Limite de saques diários excedido. Tente novamente amanhã.")
                continue

            try:
                valor_saque = valida_valores(
                    float(input("Informe o valor do saque R$: "))
                )
            except ValueError as e:
                print(f"Erro: {e}")
                continue

            if valor_saque > limite:
                print(f"Limite de R$ {limite:.2f} de saque excedido.")
                continue

            if valor_saque > saldo:
                print(
                    f"Saldo insuficiente para saque! Saldo disponível: R$ {saldo:.2f}."
                )
                continue

            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque de R$ {valor_saque:.2f} às {datetime.now().strftime('%Y-%m-%d %H:%M')} horas.\n"
            print(
                f"Saque realizado com sucesso às {datetime.now().strftime('%Y-%m-%d %H:%M')} horas!"
            )

        case "e":
            print("\n---------------------- EXTRATO ----------------------")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"Saldo atual: R$ {saldo:.2f}")
            print(f"Consulta realizada às {datetime.now().strftime('%Y-%m-%d %H:%M')}.")
            print("----------------------------------------------------\n")

        case "q":
            print("Saindo... Obrigado por utilizar nosso sistema!")
            break

        case _:
            print("Operação inválida. Por favor, selecione uma opção válida.")
