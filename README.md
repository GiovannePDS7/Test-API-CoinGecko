# API Tests - CoinGecko

This project contains a series of automated tests for the public CoinGecko API, which provides information about cryptocurrencies, such as the current price of Bitcoin, details about Bitcoin, and error responses for invalid coins.

## Objective

The goal of this project is to test the functionalities of the CoinGecko API automatically using the `pytest` framework and the `requests` library. These tests ensure that the API responses are as expected, such as response status, data presence, and correct values.

## Test Features

The project includes three main tests:

1. **Test Bitcoin Information**:
   - Verifies that the API correctly returns the `id` field with the value `'bitcoin'`.

2. **Test Bitcoin Price**:
   - Verifies that the current Bitcoin price in USD is present in the `market_data` field of the API response.

3. **Test Non-existent Coin**:
   - Verifies that the API returns a 404 error for a non-existent coin, such as `'nonexistentcoin'`.

## Prerequisites

Before running the tests, you need to have Python installed on your machine. The project uses the `requests` and `pytest` libraries.

### Install Dependencies

1. **Clone the repository to your computer**:

```bash
git clone https://github.com/GiovannePDS7/Test-API-CoinGecko.git
```
2. **Navigate to the project folder:**:
```bash
cd Test-API-CoinGecko
```
3. **Create and activate a virtual environment (optional but recommended):**:

*On Windows:*
```python
python -m venv venv
.\venv\Scripts\activate
```
*On macOS/Linux::*
```python
python3 -m venv venv
source venv/bin/activate
```
4. **Install the dependencies:**:
```python
pip install -r requirements.txt
```
## Running the Tests

### Testing the API

*To run the tests, simply run the following command in the terminal within the project directory:*
```bash
pytest test-coin-api-gecko.py
```
*Displaying prints in the console:*
```bash
pytest test-coin-api-gecko.py -s
```
## How It Works?

1. **test_get_bitcoin_info:** Tests if the CoinGecko API correctly returns information about Bitcoin. The function validates the presence of the `id` field and checks if the value is `bitcoin`.
   
2. **test_get_bitcoin_price:** Tests retrieving the current Bitcoin price in USD. It checks if the `'market_data'` field and the subfield `'current_price'` with the value of `'usd'` are present.
   
3. **test_get_invalid_coin:** Tests the API response when trying to access a non-existent coin. The API should return a 404 error and an error message indicating that the coin was not found.
