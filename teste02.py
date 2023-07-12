import requests

def obter_endereco_por_cep(cep):
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

# Exemplo de uso da função
cep = "64053040"
endereco = obter_endereco_por_cep(cep)
if endereco:
    print("Endereço encontrado:")
    print("CEP:", endereco["cep"])
    print("Logradouro:", endereco["logradouro"])
    print("Bairro:", endereco["bairro"])
    print("Cidade:", endereco["cidade"])
    print("Estado:", endereco["estado"])
else:
    print("CEP não encontrado.")