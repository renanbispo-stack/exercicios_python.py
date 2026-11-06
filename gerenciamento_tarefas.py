lista_tarefas=[]

while True:
    a=0
    b=0
    c=-1
    op=int(input("1-Cadastrar uma tarefa.\n2-listar todas as tarefas.\n3-Marcar uma tarefa como concluída.\n4-Excluir uma tarefa.\n5-Mostrar tarefas pendentes.\n6-Mostrar quantas tarefas foram concluídas.\n7-Sair do programa.\n"))
    if op==1:
        tarefa=input("qual a terefa que voce deseja cadastrar?\n")
        for i in lista_tarefas:
            if i[0]==tarefa:
                a=1
        if a==1:
           print("esta tafera ja existe")
        if a==0:
            lista_tarefas.append([tarefa,"inconcluida"])
            print("tabeda adicionada com sucesso")  
    elif op==2:
            print("",lista_tarefas)        


    elif op==3:
        tarefa=input("qual tarefa voce quer marcar como concluida?\n")
        for i in lista_tarefas:
            
            if i[0]==tarefa and i[1]=="inconcluida":
                a=1
                b=1
                i[1]="concluida"
        if a==1 and b==1:
            
            print("marcada como concluida")
        if a==0 or b==0:
            print("ocorreu um erro.a tarefa nao existe ou ja esta concluida",a,b)
    elif op==4:
        tarefa=input("qual tarefa voce gostaria de excluir?\n") 
        for indice,i in enumerate(lista_tarefas):
            if i[0]==tarefa:
                a=1
                break
        if a==1:
            lista_tarefas.pop(indice)
            print("",lista_tarefas)
        if a==0:
            print("esta tarefa nao existe")
    elif op==5:
        for i in lista_tarefas:
            if i[1]=="inconcluida":
                print("",i[0])
    elif op==6:
        for i in lista_tarefas:
            if i[1]=="concluida":
                a+=1
                print("",i[0])   
        print(f"voce tem {a} tarefas a serem concluidas")
    elif op==7:
        break 
    else:
        print("opçao invalida")
