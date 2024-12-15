import requests
import pytest

# URL base da API CoinGecko
BASE_URL = "https://api.coingecko.com/api/v3/coins/"

def test_get_bitcoin_info():
    """
    Testa a obtenção de informações sobre o Bitcoin.
    Verifica se a API retorna o campo 'id' com o valor 'bitcoin'.
    """
    url = BASE_URL + "bitcoin"
    response = requests.get(url)

    # Verificar se a resposta é 200 OK
    assert response.status_code == 200, "Erro ao acessar a API do Bitcoin"

    data = response.json()

    # Verificar se a resposta contém o campo 'id' e se é igual a 'bitcoin'
    assert 'id' in data, "O campo 'id' não foi encontrado na resposta"
    assert data['id'] == 'bitcoin', f"ID do Bitcoin esperado: 'bitcoin', mas foi: {data['id']}"

def test_get_bitcoin_price():
    """
    Testa a obtenção do preço atual do Bitcoin.
    Verifica se o preço do Bitcoin em USD está presente na resposta.
    """
    url = BASE_URL + "bitcoin"
    response = requests.get(url)

    # Verificar se a resposta é 200 OK
    assert response.status_code == 200, "Erro ao acessar a API do preço do Bitcoin"

    data = response.json()

    # Verificar se o campo 'market_data' está presente
    assert 'market_data' in data, "'market_data' não encontrado na resposta"

    # Verificar se o preço do Bitcoin está presente em 'market_data' -> 'current_price' -> 'usd'
    assert 'current_price' in data['market_data'], "'current_price' não encontrado em 'market_data'"
    assert 'usd' in data['market_data']['current_price'], "Preço do Bitcoin em USD não encontrado"

    # Exibir o preço do Bitcoin em USD
    print(f"Valor do BTC em USD = {data['market_data']['current_price']['usd']}")  # Rodando com o parâmetro -s

def test_get_invalid_coin():
    """
    Testa a resposta da API para uma moeda inválida.
    A API deve retornar erro 404 para moedas inexistentes.
    """
    url = BASE_URL + "nonexistentcoin"  # Nome de uma moeda inválida
    response = requests.get(url)

    # Verificar se a resposta é 404 (não encontrado)
    assert response.status_code == 404, "Erro esperado: moeda inexistente, mas a resposta foi diferente"

    data = response.json()

    # Verificar se a resposta contém o campo 'error'
    assert 'error' in data, "'error' não encontrado na resposta de moeda inexistente"

