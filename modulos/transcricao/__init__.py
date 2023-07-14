import csv
from datetime import datetime, date
from modulos.pacientes import *
from modulos.consultas import *

data_atual = date.today()
data_atual = datetime.strftime(data_atual, '%d/%m/%Y')

def obter_ultimo_id_transcricao():
    with open('transcricao.csv', 'r', encoding= "utf-8") as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        linhas = list(reader)

    # Se o arquivo estiver vazio, retorna 0 como o último ID
    if not linhas:
        return 0

    # Obtém o último ID da última linha
    ultimo_id = int(linhas[-1][0])
    return ultimo_id

def gerar_novo_id_transcricao():
    ultimo_id = obter_ultimo_id_transcricao()
    novo_id = ultimo_id + 1
    return novo_id

def salvar_transcricao(paciente = '', consulta = '', transcricao = "", palavras_chave = "" ):
    id_transcricao = gerar_novo_id_transcricao()    
    id_paciente = buscar_id_por_nome(paciente)
    paciente = paciente
    id_consulta = consulta  
    transcricao = transcricao
    data = data_atual
    palavras_chave = palavras_chave

    transcriao_consulta = [id_transcricao, id_paciente, paciente, id_consulta, transcricao, data, palavras_chave]

    with open('transcricao.csv', 'a', encoding= "utf-8", newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(transcriao_consulta)          
    print("Transcrição salva com sucesso!")
    return True
    
#Testes
#salvar_transcricao(paciente= 'Oswaldo Jales', consulta= 2 ,transcricao = "Lorem ipsum dolor sit amet. 33 asperiores architecto qui enim voluptas et excepturi consequatur id ipsa unde est quas internos ut pariatur eius? Ad tempore tempora non porro dolorum ut laborum internos? At molestiae repudiandae quo similique galisum qui suscipit voluptatum aut quis atque ab inventore Quis et vero mollitia ea enim quam. Non libero velit At consectetur atque eum quod eaque qui deserunt officiis ad nulla earum sed nesciunt accusantium.", palavras_chave = "teste" )
#salvar_transcricao(paciente= 'Oswaldo Jales', consulta= 4 ,transcricao = "At voluptas officia id ipsum incidunt aut impedit laboriosam id illum dolores id reiciendis esse qui assumenda porro. Ut deleniti consequatur nam sunt atque qui dolorem sunt. Et cupiditate voluptas aut atque asperiores est possimus quidem sed accusantium cupiditate!", palavras_chave = "teste" )
#salvar_transcricao(paciente= 'Amelie Maria', consulta= 1 ,transcricao = "exemplo de transcrição", palavras_chave = "teste" )
#salvar_transcricao(paciente= 'Giovanna Oliveira', consulta= 3 ,transcricao = "Ab internos molestias qui dolorum saepe rem nulla quas ut molestias minima et aliquid dolores qui tenetur consequatur. Et tempore velit vel nihil deserunt qui laborum Quis. In error nihil ab nostrum nostrum in Quis harum.", palavras_chave = "teste" )

def obter_transcrições():
    lista_transcrições = []
    with open('transcricao.csv', 'r', encoding= "utf-8") as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            lista_transcrições.append(linha)

    return lista_transcrições

#Teste
# print(f'{obter_transcrições()}')

def buscar_transcrições_paciente(nome_paciente):
    lista_transcrições = []
    with open('transcricao.csv', 'r', encoding= "utf-8") as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            if nome_paciente.lower() in linha[2].lower():
                lista_transcrições.append(linha)

    return lista_transcrições

#Teste
#print(f"{buscar_transcrições_paciente('Oswaldo Jales Coêlho')}")

def buscar_transcrições_id_paciente(id):
    id = str(id)
    lista_transcrições = []
    with open('transcricao.csv', 'r', encoding= "utf-8") as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            if id == linha[1]:
                lista_transcrições.append(linha)

    return lista_transcrições

#Teste
#print(f"{buscar_transcrições_id_paciente(2)}")

def buscar_transcrições_id_consulta(id):
    id = str(id)
    lista_transcrições = []
    with open('transcricao.csv', 'r', encoding= "utf-8") as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            if id == linha[3]:
                lista_transcrições.append(linha)

    return lista_transcrições

#Teste
#print(f"{buscar_transcrições_id_consulta(1)}")

def buscar_transcrições_id_transcrição(id):
    id = str(id)
    lista_transcrições = []
    with open('transcricao.csv', 'r', encoding= "utf-8") as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            if id == linha[0]:
                lista_transcrições.append(linha)

    return lista_transcrições

#Teste
#print(f"{buscar_transcrições_id_transcrição(1)}")

