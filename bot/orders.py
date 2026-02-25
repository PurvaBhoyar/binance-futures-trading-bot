from bot.logging_config import logger

def place_order(client, symbol, side, order_type, quantity, price=None, stop_price=None):
    try:
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "quantity": quantity,
        }

        if order_type.upper() == "MARKET":
            params["type"] = "MARKET"
        elif order_type.upper() == "LIMIT":
            params.update({"type": "LIMIT", "price": str(price), "timeInForce": "GTC"})
        elif order_type.upper() == "STOP_LIMIT":
            params.update({"type": "STOP", "price": str(price), "stopPrice": str(stop_price), "timeInForce": "GTC"})

        # Execute order
        response = client.futures_create_order(**params)
        
        # LOG AND FLUSH IMMEDIATELY
        logger.info(f"SUCCESS: {params} -> Response: {response}")
        for handler in logger.handlers:
            handler.flush()
            
        return response
    except Exception as e:
        logger.error(f"FAILURE: {symbol} - Error: {e}")
        for handler in logger.handlers:
            handler.flush()
        raise e