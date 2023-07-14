from datetime import datetime, date
import requests

data_atual = date.today()
data_atual = datetime.strftime(data_atual, '%d/%m/%Y')

def validar_cpf(cpf):
    # Remover caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verificar se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

    # Cálculo do primeiro dígito verificador
    soma = 0
    peso = 10
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = soma % 11
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto

    # Verificar o primeiro dígito verificador
    if digito_verificador_1 != int(cpf[9]):
        return False

    # Cálculo do segundo dígito verificador
    soma = 0
    peso = 11
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = soma % 11
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto

    # Verificar o segundo dígito verificador
    if digito_verificador_2 != int(cpf[10]):
        return False

    return True

def obter_endereco_por_cep(cep=''):
    url = f"https://brasilapi.com.br/api/cep/v1/{cep}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        endereco = {
            "cep": data["cep"],
            "logradouro": data["street"],
            "bairro": data["neighborhood"],
            "cidade": data["city"],
            "estado": data["state"]
        }
        return endereco
    else:
        return None

