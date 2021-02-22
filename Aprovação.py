#

print("Digite 2 notas, uma de cada vez, e pressione Enter")

num1 = float(input("Digite uma note de 0 a 10. "))
num2 = float(input("Digite outra nota de 0 a 10. "))

if( num1 < 0 ):
    num1 = 0

if( num1 > 10):
    num1 = 10

if( num2 < 0 ):
    num2 = 0

if( num2 > 10):
    num2 = 10

media = float( (num1 + num2) / 2 )

if(media >= 6):
    print('parabéns voce foi aprovado! Média:', media)
else:
    if(media > 1 ) : 
        print("Calma, você tem a prova de recuperação, Média: ", media)
    else:
        print("Infelizmente você foi reprovado! Média: ", media)
        
