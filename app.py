# -*- coding: utf-8 -*-
"""
Classificador de Consumo de Água
Campanha de conscientização ambiental - Companhia de Saneamento

O programa solicita o tipo de imóvel e o consumo mensal (m³)
e exibe uma mensagem educativa de acordo com o perfil de consumo.
"""

LIMITE_ECONOMICO = 10   # m³ (apenas apartamento)
LIMITE_RESIDENCIAL = 25  # m³ (apartamento e casa)
TIPOS_VALIDOS = ("comercial", "casa", "apartamento")


def ler_tipo_imovel():
    """Pede o tipo de imóvel até que o usuário informe uma opção válida."""
    while True:
        tipo = input("Tipo de imóvel (comercial / casa / apartamento): ").strip().lower()
        if tipo in TIPOS_VALIDOS:
            return tipo
        print("⚠️  Tipo inválido! Digite: comercial, casa ou apartamento.")


def ler_consumo():
    """Pede o consumo mensal (m³) até que o usuário informe um número válido."""
    while True:
        entrada = input("Consumo mensal de água (m³): ").strip().replace(",", ".")
        try:
            consumo = float(entrada)
        except ValueError:
            print("⚠️  Valor inválido! Digite um número (ex.: 12.5).")
            continue
        if consumo < 0:
            print("⚠️  O consumo não pode ser negativo.")
            continue
        return consumo


def classificar_consumo(tipo, consumo):
    """Aplica as regras de negócio e retorna a mensagem correspondente."""
    if tipo == "comercial":
        return "Tarifa comercial aplicada – consulte o plano corporativo."
    elif tipo == "apartamento" and consumo < LIMITE_ECONOMICO:
        return "Consumo econômico – excelente controle de água!"
    elif tipo in ("apartamento", "casa") and consumo <= LIMITE_RESIDENCIAL:
        return "Consumo moderado – dentro do padrão residencial."
    else:
        return "Consumo excessivo – adote medidas de economia e verifique vazamentos."


def main():
    print("=" * 55)
    print("💧 CLASSIFICADOR DE CONSUMO DE ÁGUA 💧")
    print("=" * 55)

    tipo = ler_tipo_imovel()
    consumo = ler_consumo()

    print("\n📋 Resultado da análise:")
    print(classificar_consumo(tipo, consumo))


if __name__ == "__main__":
    main()
