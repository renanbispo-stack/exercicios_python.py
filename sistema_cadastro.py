pacientes=[]
b=-1
c=0
while True:
    a=0
    b=-1
    c=0
    op_1=int(input("1-cadastrar\n2-consultar\n3-editar\n4-excluir paciente\n"))

    if op_1==1:
        nome=input("qual o nome do paciente?\n")
        for i in pacientes:
            
            if nome==i:
                a=1
        if a==0 :  
            pacientes.append(nome)
            print(f"paciente {nome} cadastrado")

        else: print("usuario ja cadastrado")

    if op_1==2:
        nome_=input("nome do paciente \n")
        for i in pacientes:
            
           
            if nome_ ==i:
                a=1
                 
        if a==1:
            print("paciente cadatrado")
        else:print("paciente nao cadastrado")   
        
    if op_1==3:
        nome=input(" diga o nome do paciente\n")
        for i in pacientes:
            b+=1
            if nome==i:
                novo_nome=input("fale o novo nome\n") 
                pacientes[b]=novo_nome   
                c=1
        if c==0:
            print("usuario nao achado")

    if op_1==4:        
        nome=input("qual o nome do paciente?\n")
        for i in pacientes:
            b+=1
            if nome==i:
                pacientes.pop(b)
                a=1
        if a==0:
            print("paciente nao encontrado")        