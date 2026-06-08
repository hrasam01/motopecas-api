import requests


class BrasilApi:

    BASE_URL = "https://brasilapi.com.br/api/cep/v1"

    @staticmethod
    def buscar_cep(cep: str):

        resposta = requests.get(
            f"{BrasilApi.BASE_URL}/{cep}"
        )

        if resposta.status_code != 200:
            return None

        return resposta.json()
