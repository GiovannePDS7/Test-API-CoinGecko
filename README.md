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
