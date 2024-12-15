# Testes de API - CoinGecko

Este projeto contém uma série de testes automatizados para a API pública do CoinGecko, que fornece informações sobre criptomoedas, como o preço atual do Bitcoin, detalhes sobre o Bitcoin e a resposta de erro para moedas inválidas.

## Objetivo

O objetivo deste projeto é testar as funcionalidades da API CoinGecko de forma automatizada usando o framework `pytest` e a biblioteca `requests`. Esses testes garantem que as respostas da API estejam de acordo com o esperado, como status de resposta, presença de dados e valores corretos.

## Funcionalidades dos Testes

O projeto inclui três testes principais:

1. **Testar informações do Bitcoin**:
   - Verifica se a API retorna corretamente o campo `id` com o valor `'bitcoin'`.

2. **Testar o preço do Bitcoin**:
   - Verifica se o preço do Bitcoin em USD está presente no campo `market_data` da resposta da API.

3. **Testar moeda inexistente**:
   - Verifica se a API retorna um erro 404 para uma moeda inválida, como `'nonexistentcoin'`.

## Pré-requisitos

Antes de executar os testes, você precisa ter o Python instalado em sua máquina. O projeto utiliza as bibliotecas `requests` e `pytest`.

### Instalar as dependências

1. **Clone o repositório para o seu computador**:

```bash
git clone https://github.com/GiovannePDS7/Test-API-CoinGecko.git
```
2. **Acesse a pasta**:
```bash
cd Test-API-CoinGecko
```
3. **Crie e ative um ambiente virtual (opcional, mas recomendado)**:

*No Windows:*
```python
python -m venv venv
.\venv\Scripts\activate
```
*No macOS/Linux::*
```python
python3 -m venv venv
source venv/bin/activate
```
4. **Instale as dependências**:
```python
pip install -r requirements.txt
```
## Executando os Testes

### Testando API

*Para executar os testes, basta rodar o seguinte comando no terminal dentro do diretório do projeto:*
```bash
pytest test-coin-api-gecko.py
```
*Exibindo prints no console:*
```bash
pytest test-coin-api-gecko.py -s
```
## Como Funciona?

1. **test_get_bitcoin_info:** Testa se a API do CoinGecko retorna informações sobre o Bitcoin corretamente. A função valida a presença do campo `id` e verifica se o valor é `bitcoin`.
   
2. **test_get_bitcoin_price:** Testa a obtenção do preço atual do Bitcoin em USD. Ele verifica se o campo `'market_data'` e o subcampo `'current_price'` com o valor de `'usd'` estão presentes.
   
3. **test_get_invalid_coin:** Testa a resposta da API quando você tenta acessar uma moeda inexistente. A API deve retornar um erro 404 e uma mensagem de erro indicando que a moeda não foi encontrada.
