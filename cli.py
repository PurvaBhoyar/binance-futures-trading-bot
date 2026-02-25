import typer
from rich.console import Console
from bot.client import get_binance_client
from bot.orders import place_order
from bot.logging_config import logger
console = Console()
app = typer.Typer(no_args_is_help=True)

@app.command()
def main(
    symbol: str = typer.Option(..., "--symbol"),
    side: str = typer.Option(..., "--side"),
    order_type: str = typer.Option(..., "--type"),
    qty: float = typer.Option(..., "--qty"),
    price: float = typer.Option(0.0, "--price"),
    stop: float = typer.Option(0.0, "--stop")  # Added explicitly here
):
    """
    Finalized Trading Bot CLI with Stop-Limit and Rich UI.
    """
    # Validation for Stop-Limit
    if order_type.upper() == "STOP_LIMIT" and stop == 0.0:
        console.print("[bold red]Error:[/bold red] --stop is required for STOP_LIMIT orders.")
        raise typer.Exit()

    # Confirmation
    if not typer.confirm(f"🚀 Place {order_type} {side} for {qty} {symbol}?"):
        raise typer.Abort()

    client = get_binance_client()
    try:
        res = place_order(client, symbol, side, order_type, qty, price, stop)
        
        # Check for standard order or conditional (algo) order
        if isinstance(res, dict):
            order_id = res.get('orderId') or res.get('algoId')
            if order_id:
                console.print(f"[bold green]✅ Success![/bold green] Order ID: [cyan]{order_id}[/cyan]")
                return
        
        console.print(f"[bold yellow]⚠️ Order Response:[/bold yellow] {res}")
    except Exception as e:
        console.print(f"[bold red]❌ Error:[/bold red] {e}")

if __name__ == "__main__":
    app()