import csv
from datetime import datetime, date, timedelta
from pacientes import *

data_atual = date.today()
data_atual = datetime.strftime(data_atual, '%d/%m/%Y')

def obter_ultimo_id_consultas():
    with open('consultas.csv', 'r', encoding= "utf-8") as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        linhas = list(reader)

    # Se o arquivo estiver vazio, retorna 0 como o último ID
    if not linhas:
        return 0

    # Obtém o último ID da última linha
    ultimo_id = int(linhas[-1][0])
    return ultimo_id

def gerar_novo_id_consultas():
    ultimo_id = obter_ultimo_id_consultas()
    novo_id = ultimo_id + 1
    return novo_id

def marcar_consulta(nome_paciente = '', data_consulta = '', hora_consulta ='', duração_consulta = '', status_consulta = ' '):
    id_consulta = int(gerar_novo_id_consultas())     
    nome_paciente = nome_paciente
    id_paciente = buscar_id_por_nome(nome_paciente)
    data_marcação = data_atual
    data_consulta = data_consulta
    hora_consulta = hora_consulta
    duração_consulta = duração_consulta
    status_consulta = status_consulta
    ## Status possíveis: Marcado, Cancelado, Reagendado, Realizado, Não realizado

    consulta = [id_consulta, id_paciente, nome_paciente, data_marcação, data_consulta, hora_consulta, duração_consulta, status_consulta]

    with open('consultas.csv', 'a', encoding= "utf-8",newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(consulta)
    print("Consulta marcada com sucesso!")
    return True

def obter_consultas():
    lista_consultas = []
    with open('consultas.csv', 'r', encoding= "utf-8") as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            lista_consultas.append(linha)

    return lista_consultas

def buscar_consultas_paciente(nome_paciente):
    lista_consultas = []
    with open('consultas.csv', 'r', encoding= "utf-8") as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            if nome_paciente.lower() in linha[2].lower():
                lista_consultas.append(linha)

    return lista_consultas

def buscar_consultas_id_paciente(id_paciente):
    id_paciente = str(id_paciente)
    lista_consultas = []
    with open('consultas.csv', 'r', encoding= "utf-8") as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            if id_paciente == linha[1]:
                lista_consultas.append(linha)

    return lista_consultas

def buscar_consultas_id_consulta(id_consulta):
    id_consulta = str(id_consulta)
    lista_consultas = []
    with open('consultas.csv', 'r', encoding= "utf-8") as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            if id_consulta == linha[0]:
                lista_consultas.append(linha)

    return lista_consultas

def buscar_consultas_por_data(data):
    lista_consultas = []
    data = datetime.strptime(data, "%d/%m/%Y")

    with open('consultas.csv', 'r', encoding= "utf-8") as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            data_linha = linha[4]
            if data == datetime.strptime(data_linha, "%d/%m/%Y"):
                lista_consultas.append(linha)

    return lista_consultas

#TESTES
marcar_consulta( nome_paciente = 'Amelie Maria', data_consulta = '16/04/2023', hora_consulta ='18:00', duração_consulta = '1h', status_consulta = 'Marcada')
marcar_consulta( nome_paciente = 'Oswaldo Jales', data_consulta = '15/04/2023', hora_consulta ='18:00', duração_consulta = '1h', status_consulta = 'Marcada')
marcar_consulta( nome_paciente = 'Giovanna Oliveira', data_consulta = '16/04/2023', hora_consulta ='15:00', duração_consulta = '1h', status_consulta = 'Marcada')
marcar_consulta( nome_paciente = 'Oswaldo Jales', data_consulta = '15/05/2023', hora_consulta ='18:00', duração_consulta = '1h', status_consulta = 'Marcada')

print(f"{obter_consultas()}")
#print(f"{buscar_consultas_paciente('Oswaldo Jales Coêlho')}")
#print(f"{buscar_consultas_id_paciente(1)}")
#print(f"{buscar_consultas_id_consulta(4)}")
#print(f"{buscar_consultas_por_data('15/04/2023')}")