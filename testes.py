import csv
from datetime import datetime, date

def buscar_paciente_por_id(id_paciente):
    with open('pacientes.csv', 'r') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            if linha[0] == id_paciente:
                nome = linha[1]
                return id_paciente, nome

    return None

# Exemplo de uso:
#id_busca = input(2)
#resultado = buscar_paciente_por_id(id_busca)

#if resultado:
#    id_paciente, nome_paciente = resultado
#    print("Paciente encontrado:")
#    print("ID:", id_paciente)
#    print("Nome:", nome_paciente)
#else:
#    print("Paciente não encontrado.")

def obter_pacientes():
    lista_pacientes = []

    with open('pacientes.csv', 'r') as arquivo_csv:
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
    with open('pacientes.csv', 'r') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            if nome_paciente.lower() in linha[1].lower():
                return linha[0]

    return None

# Exemplo de uso:
#nome_busca = input("Digite o nome do paciente que deseja buscar: ")
#id_paciente = buscar_id_por_nome(nome_busca)

#if id_paciente:
#    print("ID do paciente {}: {}".format(nome_busca, id_paciente))
#else:
#    print("Paciente não encontrado.")


def buscar_id_por_cpf(cpf):
    with open('pacientes.csv', 'r') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            if cpf in linha[5]:
                return linha[0]

    return None

#id_paciente = buscar_id_por_cpf('00465696341')

#if id_paciente:
#    print(f"ID do paciente {id_paciente}")
#else:
#    print("Paciente não encontrado.")


def obter_nomes_pacientes():
    nomes_pacientes = []

    with open('pacientes.csv', 'r') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            nomes_pacientes.append(linha[1])

    return nomes_pacientes

# Exemplo de uso:
#lista_nomes_pacientes = obter_nomes_pacientes()

#if lista_nomes_pacientes:    
#    for nome_paciente in lista_nomes_pacientes:
#        print(nome_paciente)
#else:
#    print("Nenhum paciente encontrado.")