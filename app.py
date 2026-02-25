import streamlit as st
from bot.client import get_binance_client
from bot.orders import place_order
from bot.logging_config import logger # Import the shared logger

st.title("🚀 Primetrade AI Bot Dashboard")

# Form logic
with st.form("trade_form"):
    symbol = st.text_input("Symbol", value="BTCUSDT")
    side = st.selectbox("Side", ["BUY", "SELL"])
    o_type = st.selectbox("Type", ["MARKET", "LIMIT", "STOP_LIMIT"])
    qty = st.number_input("Quantity", value=0.01, format="%.3f")
    price = st.number_input("Price (for Limit/Stop)", value=0.0)
    stop = st.number_input("Stop Price", value=0.0)
    submit = st.form_submit_button("Execute Trade")

if submit:
    try:
        client = get_binance_client()
        res = place_order(client, symbol, side, o_type, qty, price, stop)
        st.success(f"Order Placed! ID: {res.get('orderId') or res.get('algoId')}")
    except Exception as e:
        st.error(f"Error: {e}")