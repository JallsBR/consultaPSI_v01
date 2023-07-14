import csv
from datetime import datetime, date
from modulos.valida import *

data_atual = date.today()
data_atual = datetime.strftime(data_atual, '%d/%m/%Y')

def obter_ultimo_id_pacientes():
    with open('pacientes.csv', 'r', encoding= "utf-8") as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        linhas = list(reader)

    # Se o arquivo estiver vazio, retorna 0 como o último ID
    if not linhas:
        return 0

    # Obtém o último ID da última linha
    ultimo_id = int(linhas[-1][0])
    return ultimo_id

def gerar_novo_id_pacientes():
    ultimo_id = obter_ultimo_id_pacientes()
    novo_id = ultimo_id + 1
    return novo_id

def obter_nomes_pacientes():
    nomes_pacientes = []

    with open('pacientes.csv', 'r', encoding= "utf-8") as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            nomes_pacientes.append(linha[1])
    nomes_pacientes = sorted(nomes_pacientes)
    return nomes_pacientes

def buscar_paciente_por_id(id_paciente):
    with open('pacientes.csv', 'r', encoding= "utf-8") as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            if linha[0] == id_paciente:
                nome = linha[1]
                return id_paciente, nome

    return None

def obter_pacientes():
    lista_pacientes = []

    with open('pacientes.csv', 'r', encoding= "utf-8") as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            lista_pacientes.append(linha)

    return lista_pacientes

# Exemplo de uso:
#lista_pacientes = obter_pacientes()
#
#if lista_pacientes:
#    print("Lista de Pacientes:")
#    for paciente in lista_pacientes:
#        print("ID:", paciente[0])
#        print("Nome:", paciente[1])
#        print("Nascimento:", paciente[2])
#        print("Data deCadastro:", paciente[3])
#        print("Telefone:", paciente[4])
#        print("CPF:", paciente[5])
#        print("E-mail:", paciente[6])
#        print("Endereço:", paciente[7])
#        print("Convenio:", paciente[8])
#        print("---------")
#else:
#    print("Nenhum paciente encontrado.")

def buscar_id_por_nome(nome_paciente):
    with open('pacientes.csv','r', encoding= "utf-8") as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            if nome_paciente.lower() in linha[1].lower():
                return linha[0]

    return None

def buscar_id_por_cpf(cpf):
    with open('pacientes.csv', 'r',encoding= "utf-8") as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            if cpf in linha[5]:
                return linha[0]

    return None


def cadastrar_paciente(nome='', data_de_nascimento='', telefone = '', email= '', cep = '', endereço_complemento = '', convenio = '', numero_convenio = '', cpf = ''):
    
    id_paciente = gerar_novo_id_pacientes()
    nome = nome.strip().title()
    data_de_nascimento = data_de_nascimento
    data_cadastro_paciente = data_atual
    telefone = telefone
    email = email.strip().lower()
    cep = cep
    endereço = obter_endereco_por_cep(cep)
    endereço_complemento = endereço_complemento
    endereço['Complemento'] = endereço_complemento
    convenio = convenio
    numero_convenio = numero_convenio
    if convenio:
        convenio = {
            'Convenio'   :  convenio,
            'Número'  : numero_convenio            
        }
    else:
        convenio = 'Particular'

    if buscar_id_por_cpf(cpf) or buscar_id_por_nome(nome):
        print ('Paciente já possui cadastro')
        return False

    if validar_cpf(cpf)==False:
        print ('CPF Inválido')
        return False
    
    paciente = [id_paciente, nome, data_de_nascimento, data_cadastro_paciente, telefone, cpf, email, endereço, convenio]

    with open('pacientes.csv', 'a', encoding= "utf-8",newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(paciente)
    print ('Paciente cadastrado com sucesso!')
    return True

#Testes
#cadastrar_paciente(nome='Oswaldo Jales', data_de_nascimento='17/03/1984', telefone = '86999180435', email= 'oswaldo@gmail.com', cep = '64057-223', endereço_complemento = 'Número 4277, Bloco Athena 104', convenio = 'Unimed', numero_convenio = '002', cpf = '35247256948')
#cadastrar_paciente(nome='Amelie Maria', data_de_nascimento='05/04/2014', telefone = '86999180478', email= 'amelie@gmail.com', cep = '64201-320', endereço_complemento = 'Número 4277, Bloco Zeus 304', convenio = 'Humana Saude', numero_convenio = '962', cpf = '35373967246')
#cadastrar_paciente(nome='Giovanna Oliveira', data_de_nascimento='14/10/1985', telefone = '86999180492', email= 'gold@gmail.com', cep = '64012-805', endereço_complemento = 'Número 4277, Bloco Era 204', cpf = '73110701472')


#print(f'{obter_nomes_pacientes()}')
