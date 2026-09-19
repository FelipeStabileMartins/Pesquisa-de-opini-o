# Tudo Web - pesquisa de opinião
# Felipe 



print( )
print("Bem-vindo à pesquisa de opinião do Tudo Web!")

EXCELENTE = 0
BOM = 0
RUIM = 0




for opiniao in range(1,51):
    print ( "Numero de entrevistados", opiniao )

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    opiniao = input("Digite sua opinião sobre o Tudo Web (1 a 3): ")

    match opiniao:
        case "1" | "Um" | "um" | "UM":
            print("EXCELENTE")
            EXCELENTE += 1 
        case "2" | "Dois" | "dois" | "DOIS":
            print("BOM")
            BOM += 1
        case "3" | "tres" | "Tres" | "TRES":
            print("RUIM")
            RUIM += 1
        case _:
            print( "INEXISTENTE, TENTE DE NOVO")
        

    print( )
    print ("Resultado ate agora: ")
    print ("Quantidade de respostas EXCELENTE:", EXCELENTE )
    print ("Quantidade de respostas BOM:", BOM )
    print ("Quantidade de respostas RUIM:", RUIM )
    print( )
    print("OBRIGADO POR PARTICIPAR")
    print( )

print() 
print("Resultado final")
print ("Resultado ate agora: ")
print ("Quantidade de respostas EXCELENTE:", EXCELENTE )
print ("Quantidade de respostas BOM:", BOM )
print ("Quantidade de respostas RUIM:", RUIM )












    
        