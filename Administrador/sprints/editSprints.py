import json
import os

caminho_sprint = "././data/sprint.json"
caminho_turma = "././data/turmas.json"

# Método para criar sprints
def editSprints():
    with open(caminho_turma, 'r') as turmas:
        turmas = json.load(turmas)
    
    x = 1
    for turma in turmas:
        print(f'{x} - {turma["identificacao"]}')
        x +=1
    
    while True:
        try:
            indice_turma_escolhida = int(input('\nDigite a turma referente a sprint desejada: ')) - 1
            if indice_turma_escolhida >= (x - 1) or indice_turma_escolhida + 1 == 0:
                raise ValueError
            else:
                break
        except ValueError:
            print("Opção inválida - Tente novamente")
    
    
    id_turma = str(turmas[indice_turma_escolhida]["id_turma"])
    
    with open(caminho_sprint, 'r') as sprints:
        sprints = json.load(sprints)
    
    sprints_turmas = []
    for sprint in sprints:
        if sprint['id_turma'] == id_turma:
            sprints_turmas.append(sprint)
    
    y = 1
    for sprint in sprints_turmas:
        print(f'{y} - {sprint["identificacao"]}')
        y+=1
    
    
    
    while True:
        try:
            a = int(input('\nDigite a sprint que você deseja editar: ')) - 1
            if a >= (y - 1) or a + 1 == 0:
                raise ValueError
            else:
                break
        except ValueError:
            print("Opção inválida - Tente novamente")
    
    
    
    id_sprint = sprints_turmas[a]["id_sprint"]
    indice_sprint_escolhida = sprints.index(sprints_turmas[a])
    
    del(sprints[indice_sprint_escolhida])
    
    identificacao_sprint = input("Entre com a identificacao da sprint: ")
    while True:
        data_inicio = str(input('Entre com a data inicial (dd/mm/aaaa):'))
        if len(data_inicio) == 10 and data_inicio[2] == '/' and data_inicio[5] == '/':
            dia = (data_inicio.split('/')[0]) #// 1000000 
            mes = (data_inicio.split('/')[1])#%1000000//10000
            ano = (data_inicio.split('/')[2]) #% 10000
            
            if dia.isdigit() and mes.isdigit() and ano.isdigit():
                dia = int(dia)
                mes = int(mes)
                ano = int(ano)
            
            
                if ano >= 1:
                    vd = 1
                    if mes < 1 or mes > 12 or dia < 1 or dia > 31:
                        vd = 0
                    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
                        vd = 0
                    elif mes == 2:
                        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
                            if dia > 29:
                                vd = 0
                        else:
                            if dia > 28:
                                vd = 0
                else:
                    vd = 0
                if vd == 0:
                    print('Data inválida')
                else:
                    print('Data inicial salva')
                break
            else:
                print('Formato de data inválida digite somente numeros')
        else: 
            print('Data inválida digite conforme dd/mm/aaaa ')

    # Solicitar a data final até que seja maior que a data de inicio
    while True:
        data_final = str(input('Entre com a data final (dd/mm/aaaa):'))
        if len(data_final) == 10 and data_final[2] == '/' and data_final[5] == '/':
            dia = (data_final.split('/')[0]) #// 1000000
            mes = (data_final.split('/')[1])#%1000000//10000
            ano = (data_final.split('/')[2])# % 10000
            
            if dia.isdigit() and mes.isdigit() and ano.isdigit():
                dia = int(dia)
                mes = int(mes)
                ano = int(ano)
            
            
                if ano >= 1:
                    vd = 1
                    if mes < 1 or mes > 12 or dia < 1 or dia > 31:
                        vd = 0
                    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
                        vd = 0
                    elif mes == 2:
                        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
                            if dia > 29:
                                vd = 0
                        else:
                            if dia > 28:
                                vd = 0
                else:
                    vd = 0
                if vd == 0:
                    print('Data inválida')
                else:
                    if data_inicio >= data_final:
                        print('Data inicial maior que a data final \nDigite uma data maior que a inicial')
                    else:
                        print('Data final Salva')
                        break
            else:
                print('Formato de data inválida digite somente numeros')
        else: 
            print('Data inválida digite conforme dd/mm/aaaa ')
            
    nova_sprint = {
        'id_sprint': id_sprint,
        'identificacao': identificacao_sprint,
        'id_turma': id_turma,
        'inicio': data_inicio,
        'final' : data_final
        
    }
    
    sprints.append(nova_sprint)
    
    with open(caminho_sprint, "w") as spr:
        json.dump(sprints, spr)