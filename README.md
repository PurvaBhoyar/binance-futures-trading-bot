# Binance Futures Trading Bot (USDT-M)

A Python-based trading bot built for the Binance Futures Testnet (USDT-M).  
The application follows a modular architecture for order execution, structured logging, and provides two interfaces:

- Command Line Interface (CLI)
- Web Dashboard

This project is designed to simulate futures trading workflows and test automated order placement.

---

## Features

- Market, Limit, and Stop-Limit order support
- Modular and maintainable project structure
- CLI interface built with Typer and Rich
- Lightweight web dashboard using Streamlit
- Centralized logging system
- Compatible with Binance Futures Testnet
- Handles both `orderId` and conditional `algoId` responses

---

## Project Structure

```
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   └── logging_config.py
├── app.py
├── cli.py
├── README.md
├── requirements.txt
└── trading.log
```

---

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/PurvaBhoyar/binance-futures-trading-bot.git
cd trading_bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the root directory:

```
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

---

## Command Line Interface (CLI)

The CLI supports **MARKET**, **LIMIT**, and **STOP_LIMIT** orders.

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.01
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --qty 0.01 --price 60000
```

### Stop-Limit Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type STOP_LIMIT --qty 0.01 --price 71000 --stop 70000
```

---

## Web Dashboard

Run the Streamlit web interface:

```bash
streamlit run app.py
```

---

## Logging

Execution logs are stored in:

```
trading.log
```

To maintain consistency across CLI and Streamlit processes, logger handlers are manually flushed after each API response.

---

## Technical Assumptions

### Conditional Order Handling

Stop-Limit orders on Binance Futures return an `algoId`.  
The application handles both:

- Standard `orderId`
- Conditional `algoId`

---

## Author

Purva Bhoyar
