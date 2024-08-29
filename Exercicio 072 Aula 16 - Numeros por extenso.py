# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.


lista = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
'onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: ')) 
    if 0 <= numero <= 20:
        print(lista[numero])
        resposta = str(input('deseja continuar [S/N]? ')).strip().upper()[0]
        while resposta not in 'SN':    
            resposta = str(input('deseja continuar [S/N]? ')).strip().upper()[0]
        if resposta == 'N':
            break
    else:
        print('Error')        
    
            
            



    
