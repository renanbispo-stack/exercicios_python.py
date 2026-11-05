lista_podutos=[]
faturamento=0
while True:
    a=0
    b=0
    c=100000
    op=int(input("1-Cadastrar produtos\n2-Consultar produtos\n3-registrar vendas\n4-Calcular o faturamento total\n5-mostrar os produtos com estoque baixo.\n6-Sair do programa.\n"))
   

    if op==1:
        produto=input("qual seria o nome do produto?\n")
        for i in lista_podutos:
                if i[0]==produto:
                    a=1
        if a==1:
            print("este produto ja esta cadastrado ")
        elif a==0 :  
            lista_podutos.append([produto,[],[]])
            print(f" o produto {produto} foi cadastrado")
            qtd=int(input(f"qual a quantidade de {produto} temos?\n"))
            preço=float(input("qual o preço?"))
            for i in lista_podutos:
                if i[0]==produto:
                    i[1]=qtd
                    i[2]=preço
                    print("",lista_podutos)
                    
    if op==2:
        produto=input("qual seria o produto?\n")
        for i in lista_podutos:
            if i[0]==produto:
                a=1
        if a==1:
            print("",i[0],i[1])    
        elif a==0:
            print("nao temos esse produto cadastrado")


    if op==3:
        sair_venda=0
        while True:
            a=0
            b=0
            produto=input("qual produto voce gostaria de vender?\n")
            qtd=int(input("qual seria a quantidade\n ?"))

            for i in lista_podutos:
                if i[0]==produto:
                    a=1
                    if i[1]>=qtd:
                        b=1          
                if a==1 and b==1:
                    h=i[2]
                    total=qtd*h
                    i[1]=i[1]-qtd
                    print("",total)
                    faturamento=total+faturamento
                    op_1=int(input("gostaria de vender mais algo?\n1-Sim\n2-Nao\n"))
                    if op_1==1:
                        break
                    if op_1==2:
                        sair_venda=1
                        break
                
                elif a==0 and b==1:
                    print(" nao temos esse produto cadastrado")
                elif a==1 and b==0:

                    print(" nao temos essa quantidade de produto")
                elif a==0 and b==0:           
                    print(" nao temos esse produto")
            if sair_venda==1:
                    break
    if op==4:
        print("R$",faturamento)
    
    if op==5:
        for i in lista_podutos:
            
            if i[1]<5:
                a=1
            if a==1:
                print(f"a quantidade de {i[0]} esta baixa e com {i[1]} de quantidade")

    if op==6:
        break
    elif op not in[1,2,3,4,5]:
        print("opçao invalida")        
        
            