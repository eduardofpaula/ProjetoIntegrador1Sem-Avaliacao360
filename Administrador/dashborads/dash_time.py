import pandas
import json
import os

local_sprints = '././data/sprint.json'
local_turmas =  '././data/turmas.json'
local_times = '././data/times.json'
local_usuarios = '././data/usuarios.json'
local_resposta_avaliacao = '././data/respostas_grupoAvaliacao.json'

def visualizarDashTime():
    def verificacao():
        while True:
            if os.path.exists(local_resposta_avaliacao):
                return True 

            else:
                print("Não exista avaliação para ser mostrada\n")
                print('------------------------------------------')
                return
            
    continuar = verificacao()

    def visualizarTurmas(continuar=True):
        
        with open (local_turmas,'r') as arquivo_turmas:
            turmas = json.load(arquivo_turmas)

        print("\nVisualizar Turmas:")
        x = 1
        for name in turmas:
            print(f"{x} - {name['identificacao']}")
            x = x+1
        print('0 - Voltar')
        
        while True:
            try:
                num_turmas = int(input('\nDigite qual turma deseja visualizar: '))  #deixar apenas número inteiro
                if num_turmas > x-1:
                    print('\nEssa turma não existe')
                elif num_turmas == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return 
                else:
                    break    
            except ValueError:
                print('\nOpção inválida! Tente novamente!')

        os.system('cls' if os.name == 'nt' else 'clear')
        turma_escolhida = turmas[num_turmas - 1]
        id_turma = turma_escolhida.get('id_turma')
        return id_turma
        
    def visualizarTimes(id_turma):
        
        with open(local_times) as arquivo_time:
            times = json.load(arquivo_time)
            
            print("\nVisualizar Times:")
            x = 1
            for name in times:
                if name.get('id_turma') == id_turma:
                    print(f"{x} - {name['identificacao']}")
                    x = x+1
            print('0 - Voltar')
            
            while True:
                try:
                    num_time = int(input('\nDigite qual time deseja visualizar: '))  #deixar apenas número inteiro
                    if num_time > x-1:
                        print('\nEsse time não existe')
                    elif num_time == 0:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        return 
                    else:
                        break    
                except ValueError:
                    print('\nOpção inválida! Tente novamente!')

            os.system('cls' if os.name == 'nt' else 'clear')
            time_escolhido = times[num_time]
            return time_escolhido
        
    turma = visualizarTurmas(continuar=True)
    time = visualizarTimes(turma)

    def visualizarSprint(time,turma):
        
        with open(local_sprints) as arquivo_sprint:
            sprints = json.load(arquivo_sprint)

            print("\nVisualizar Sprints:")
            x = 1
            for name in sprints:
                if name.get('id_turma') == turma:
                    print(f"{x} - {name['identificacao']}")
                    x = x+1
            print('0 - Voltar')
            
            while True:
                try:
                    num_sprint = int(input('\nDigite qual sprint deseja visualizar: '))  #deixar apenas número inteiro
                    if num_sprint > x-1:
                        print('\nEssa sprint não existe')
                    elif num_sprint == 0:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        return 
                    else:
                        break    
                except ValueError:
                    print('\nOpção inválida! Tente novamente!')

            os.system('cls' if os.name == 'nt' else 'clear')
            sprint_escolhida = sprints[num_sprint-1]
            return sprint_escolhida
        
    sprint_time = visualizarSprint(time,turma)
        
    def dashTime(sprint_time,time):
        
        with open (local_usuarios,'r') as arquivo_usuario:
            usuarios = json.load(arquivo_usuario)
            
        # with open(local_resposta_autoavaliacao) as arquivo_autoavaliação:
        #     resposta_autoavaliacao = json.load(arquivo_autoavaliação)
            
        with open(local_resposta_avaliacao) as arquivo_avaliacao:
            resposta_avaliacao = json.load(arquivo_avaliacao)
        
        competencia = ["Comunicacão e Trabalho em Equipe", "Engajamento e Proatividade", "Conhecimento e Aplicabilidade", "Entrega de Resultados com Valor Agregado", "Autogestão de Atividades"]
        id_usuarios = list()
        sum_comp_1 = 0
        sum_comp_2 = 0
        sum_comp_3 = 0
        sum_comp_4 = 0
        sum_comp_5 = 0
        
        try:
            for usuario in usuarios:
                if usuario.get('id_time') == time.get('id_time') and time.get('id_turma') == str(turma):
                    id_usuarios.append(usuario.get('id_usuario'))
            num_comp = 1
            while True:
                for comp in competencia:
                    dados_coluna = {}
                    for resposta_auto in resposta_avaliacao:
                        if resposta_auto.get('id_usuario_respondeu') in id_usuarios and resposta_auto.get('ip') == str(num_comp) and sprint_time.get('id_sprint') == resposta_auto.get ('id_sprint'):
                            if resposta_auto.get('resp') == '1':
                                sum_comp_1 += 1
                            elif resposta_auto.get('resp') == '2':
                                sum_comp_2 += 1
                            elif resposta_auto.get('resp') == '3':
                                sum_comp_3 += 1
                            elif resposta_auto.get('resp') == '4':
                                sum_comp_4 += 1
                            elif resposta_auto.get('resp') == '5':
                                sum_comp_5 += 1
                            
                    coluna = [(sum_comp_5), (sum_comp_4), (sum_comp_3), (sum_comp_2), (sum_comp_1)]
                    total = sum(coluna)
                    
                    if total != 0:
                        coluna = [(sum_comp_5/total)*100, (sum_comp_4/total)*100, (sum_comp_3/total)*100, (sum_comp_2/total)*100, (sum_comp_1/total)*100]
                    dados_coluna[sprint_time.get('identificacao')] = coluna
                    num_comp +=1
                
                    df = pandas.DataFrame(dados_coluna, index = ['Excelente', 'Muito bom', 'Bom', 'Razoável', 'Ruim'])
                    print(f"\n{comp} (%)\n")
                    print(df.round(2))
                    print('\n-----------------------\n')
                
                if num_comp > 5:
                    break
        except ValueError:
            print("\nNão existe integrantes nesse time para mostrar um dashboard")