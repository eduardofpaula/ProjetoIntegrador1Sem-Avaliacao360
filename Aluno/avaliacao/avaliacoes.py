import json
import os
from datetime import datetime


local_perguntas = '././data/perguntas_autoAvaliacao.json'
local_perguntas_grupo = '././data/perguntas_grupo_avaliacao.json'
local_resposta = '././data/respostas_autoAvaliacao.json'
local_resposta_grupo = '././data/respostas_grupoAvaliacao.json'
local_identificacao = '././data/usuarios.json'
local_sprints = '././data/sprint.json'
local_time = '././data/times.json'

def sprint_atual(id_usuario):
    x = True
    y = False

    with open( local_identificacao,'r',encoding="UTF-8") as arquivo:
        usuarios = json.load(arquivo)

        for usuario in usuarios:
            if usuario.get('id_usuario') == id_usuario:
                time_usuario = usuario['id_time']
            
    
    with open(local_time,'r',encoding="UTF-8") as arquivo:
        times = json.load(arquivo)

        for id_turma_usuario in times:
            if time_usuario == id_turma_usuario.get('id_time') :
                turma_usuario = id_turma_usuario.get('id_turma')
    
    with open(local_sprints,'r',encoding="UTF-8") as arquivo:
        sprints = json.load(arquivo)

        sprint_usuario = next((sprint for sprint in sprints if turma_usuario == sprint['id_turma']),None)
        if sprint_usuario is not None:
            z = 0
            for sprint in sprints:
                if turma_usuario == sprint.get('id_turma'):
                        
                    sprint_usuario_dados = sprints[z]
                    identificacao_sprint = sprint_usuario_dados.get('identificacao')

                    data_final_avaliacao = datetime.strptime(sprint_usuario_dados['final_avaliacao'],'%d/%m/%Y')
                    data_final = datetime.strptime(sprint_usuario_dados['final'], '%d/%m/%Y')


                    if datetime.now() <= data_final_avaliacao and datetime.now() > data_final:
                        id_sprint = sprint_usuario_dados.get('id_sprint')
                        return id_sprint, x
                    elif datetime.now() > data_final_avaliacao:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'Já passou a data limite para responder a avaliação da {identificacao_sprint}')
                        print('\n--------------------------------\n')
                        return None, y
                else:
                    z +=1
        else:
            print('\nNão existe sprint cadastrado para essa turma')
            print('\n--------------------------------\n')
            return None, y


def autoAvaliacao(id_usuario):
    
    print('Autoavaliação:')


    #loop prompt

    # Verifica se o arquivo JSON já existe
    if os.path.exists(local_perguntas):
        # Se existir, carrega as perguntas existentes
        with open(local_perguntas, 'r', encoding="UTF-8") as arquivo:
            perguntas = json.load(arquivo)
    else:
        # Se não existir, cria uma lista vazia
        perguntas = []



    # verifica se o json das respostas ja existe (se alguem ja respondeu ou não)    
    if os.path.exists(local_resposta):
            # abre o arquivo JSON
            with open(local_resposta, 'r', encoding="UTF-8") as resps:
                respostas = json.load(resps)    
    # Lista para armazenar as respostas
    else:
        respostas = []


    # Função para obter a resposta do usuário como um número inteiro entre 1 e 5
    def obter_resposta():
        while True:
            try:
                resposta = int(input("\nPor favor, avalie de 1 a 5: "))
                if resposta < 1 or resposta > 5:
                    raise ValueError
                break
            except ValueError:
                print(
                    "\nNúmero Invalido\nPor favor, insira um número inteiro entre 1 e 5.")
        return resposta


    # função para retornar o maior id das respostas
    def getNextIdResp():
        if os.path.exists(local_resposta):
            # abre o arquivo JSON
            with open(local_resposta, 'r', encoding="UTF-8") as resps:
                respostas = json.load(resps)
            ids = []
            for resposta in respostas:
                ids.append(int(resposta['id_resposta']))
            return max(ids) + 1
        else:
            return 0 
        


    # Loop para obter as respostas do participante
    for pergunta in perguntas:
        print(pergunta["descricao"])
        resposta = {'id_resposta': getNextIdResp(),
                    'ip': str(pergunta["ip"]),
                    'resp': str(obter_resposta()),
                    'id_usuario': id_usuario,
                    'id_sprint': sprint_atual(id_usuario)
                    }
        respostas.append(resposta)  
        # Salvar as respostas em um arquivo JSON
        with open(local_resposta, "w") as arquivo:
            json.dump(respostas, arquivo, indent=5) 
    print("\nRespostas salvas no sistema!.\n")
    y = False
    
def avaliacao(id_usuario, id_time):
            
    # Função para obter a resposta do usuário como um número inteiro entre 1 e 5
    def obter_resposta():
        while True:
            try:
                resposta = int(input("\nPor favor, avalie de 1 a 5: "))
                if resposta < 1 or resposta > 5:
                    raise ValueError
                break
            except ValueError:
                print(
                    "\nNúmero Invalido\nPor favor, insira um número inteiro entre 1 e 5.")
        return resposta


    # função para retornar o maior id das respostas
    def getNextIdResp():
        if os.path.exists(local_resposta_grupo):
            # abre o arquivo JSON
            with open(local_resposta_grupo, 'r', encoding="UTF-8") as resps:
                respostas = json.load(resps)
            ids = []
            for resposta in respostas:
                ids.append(int(resposta['id_resposta']))
            return max(ids) + 1
        else:
            return 0
        
        
    
    time_usuarios = []
    # Verifica se o arquivo JSON já existe
    if os.path.exists(local_identificacao):
        # Se existir, carrega as perguntas existentes
        with open(local_identificacao, 'r', encoding="UTF-8") as usu:
            usuarios = json.load(usu)
    else:
        # Se não existir, cria uma lista vazia
        usuarios = []
    for usuario in usuarios:
        if usuario['id_time'] == id_time and usuario['id_usuario'] != id_usuario:
            time_usuarios.append(usuario)
    
    #para cada usuario pertencente ao time
    for usuario in time_usuarios:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Avaliação do grupo:')
        
        print('\n Em relação a(ao) integrante {}, responda: \n'.format(usuario['identificacao']))
    
        # Verifica se o arquivo JSON já existe
        if os.path.exists(local_perguntas_grupo):
            # Se existir, carrega as perguntas existentes
            with open(local_perguntas_grupo, 'r', encoding="UTF-8") as arquivo:
                perguntas = json.load(arquivo)
        else:
            # Se não existir, cria uma lista vazia
            perguntas = []



        # verifica se o json das respostas ja existe (se alguem ja respondeu ou não)    
        if os.path.exists(local_resposta_grupo):
                # abre o arquivo JSON
                with open(local_resposta_grupo, 'r', encoding="UTF-8") as resps:
                    respostas = json.load(resps)    
        # Lista para armazenar as respostas
        else:
            respostas = []
                    
            
        # Loop para obter as respostas do participante
        for pergunta in perguntas:
            print(pergunta["descricao"])
            resposta = {'id_resposta': getNextIdResp(),
                        'ip': str(pergunta["ip"]),
                        'resp': str(obter_resposta()),
                        'id_usuario_respondeu': id_usuario,
                        'id_usuario_avaliado': usuario['id_usuario'],
                        'id_sprint': sprint_atual(id_usuario)
                        }
            respostas.append(resposta)  
            # Salvar as respostas em um arquivo JSON
            with open(local_resposta_grupo, "w") as arquivo:
                json.dump(respostas, arquivo, indent=5) 
        print("\nRespostas salvas no sistema!.\n")