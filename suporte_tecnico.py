lista_chamado=[]

while True:
    a=0
    b=0
    c=0
    n=[]
    op=int(input("\n1-Abrir chamado.\n2-Listar chamados.\n3-Consultar chamado pelo número.\n4-Alterar status (Aberto, Em andamento ou Resolvido).\n5-Excluir chamado.\n6-Mostrar quantidade de chamados por status.\n7-Sair.\n"))

    if op==1:
        Numero=int(input("qual o Numero De Identificaçao\n"))
        for i in lista_chamado:
            if i[0]==Numero:
                a=1
        if a==1:
            print("esse Numero De Identificação já consta nos nossos arquivos")
        elif a==0:
                usuario=input(f"qual e o nome do Usuário?\n")
                problema=input("descriçao do problema?\n")
                status=input("status\n")
                lista_chamado.append([Numero,[usuario],[problema],[status]])
               
    if op==2:
        print(f"{lista_chamado}")

    if op==3:
        Numero=int(input("qual o numero do chamado?\n"))

        for i in lista_chamado:
            if i[0]==Numero:
                a=1
                print(f"{[i]}")
                
        if a==0:
            print("numero de identificaçao incorreto ou nao consta no nosso cadastro")
    
    if op==4 :
        numero=int(input("QUAL O NUMERO DE IDENTIFICAÇÃO?\n"))
        for i in lista_chamado:
            if i[0]==numero : 
                status=input("QUAL O NOVO STATUS?\n")   
                i[3]=status
                a=1
                print("STATUS ALTERADO ")
        if a==0:
            print("numero de indentificaçao errado\n")
    if op==5:
        numero=int(input("qual e o Numero De Identficaçao?\n"))
        for indice, i in enumerate (lista_chamado):
            if i[0]==numero:
                a=1
                break

        if a==1:
            lista_chamado.pop(indice)
        elif a==0:
            print("nao temos esse numero de identificaçao")
    
    if op==6:
        status=input("qual e o status que voce deseja pesquisar?")
        for i in lista_chamado:
          if i[3]==status:
            a=a+1
        print(f"{a}")
       
               

    if op==7:
        break    