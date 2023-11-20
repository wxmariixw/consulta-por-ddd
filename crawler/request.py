import requests
import pandas as pd
import time

def get_ddd():
    numeros_ddd = [11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 27, 28, 31, 32, 33, 34, 35, 37, 38, 41, 42, 43,
                   44, 45, 46, 47, 48, 49, 51, 53, 54, 55, 61, 62, 63, 64, 65, 66, 67, 68, 71, 73, 74, 75, 77, 79,
                   82, 83, 81, 87, 86, 89, 84, 98, 99, 91, 93, 94, 92, 97, 96, 69, 95]
    lista_cidades = []

    for ddd in numeros_ddd:
        print(ddd)
        url = f"https://brasilapi.com.br/api/ddd/v1/{ddd}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            time.sleep(2)
            for cidade in data["cities"]:
                entrada_cidade = {
                    "ddd": ddd,
                    "cidade": cidade,
                    "estado": data["state"]
                }
                lista_cidades.append(entrada_cidade)

        else:
            print(f"Erro: {response.status_code}")

    df_cidades = pd.DataFrame(lista_cidades)
    print(df_cidades)

    tabela = "cities"
    schema = "cities"
    conexao = "postgresql://postgres:postgres@localhost:5432/grandfinale"
    
    df_cidades.to_sql(tabela, conexao, schema)

get_ddd()