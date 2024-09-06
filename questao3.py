# questao3.py

import json

# Exemplo de dados (substitua com dados reais)
data = '''
{
    "faturamento": [
        {"dia": "2024-01-01", "valor": 1000},
        {"dia": "2024-01-02", "valor": 2000},
        {"dia": "2024-01-03", "valor": 1500}
    ]
}
'''
faturamento = json.loads(data)["faturamento"]

valores = [item["valor"] for item in faturamento]
media_mensal = sum(valores) / len(valores) if valores else 0

menor = min(valores) if valores else 0
maior = max(valores) if valores else 0
dias_acima_da_media = len([valor for valor in valores if valor > media_mensal])

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Número de dias acima da média: {dias_acima_da_media}")
