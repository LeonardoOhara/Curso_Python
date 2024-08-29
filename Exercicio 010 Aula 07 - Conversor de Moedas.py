# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar considerando a cotação atual .

import requests
requisicao = requests.get("http://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
requisicao_dic = requisicao.json()
cotacao_dollar = requisicao_dic["USDBRL"]["bid"]

x = (float(input("Conversor de Real para Dollar,\nDigite aqui o valor em real R$ ")))
# Para converter a moeda é preciso dividi a variavel "cotacao_dollar"
# nos EUA se usa  o ponto '.' e não a virgula.
s = x/float(cotacao_dollar)
print(f'O valor digitado em reais foi de {x:.1f} reais com a cotação do dollar hoje está em {float(cotacao_dollar):.1f} Dollar')
if s <= 1.0:
    print(f'O valor convertido foi de U$$ {s:.2f} cents')
else:
    print(f'O valor convertido foi de U$$ {s:.2f} dollar')

