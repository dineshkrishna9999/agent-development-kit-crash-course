from datetime import datetime
import random

from google.adk.agents import Agent


def get_stock_price(ticker: str) -> dict:
    """Retrieves mock stock price data for demonstration purposes."""
    print(f"--- Tool: get_stock_price called for {ticker} ---")

    # Mock stock data for common tickers
    mock_stocks = {
        "AAPL": {"base_price": 175.00, "name": "Apple Inc."},
        "GOOGL": {"base_price": 140.00, "name": "Alphabet Inc."},
        "GOOG": {"base_price": 140.00, "name": "Alphabet Inc."},
        "MSFT": {"base_price": 410.00, "name": "Microsoft Corporation"},
        "TSLA": {"base_price": 180.00, "name": "Tesla Inc."},
        "META": {"base_price": 480.00, "name": "Meta Platforms Inc."},
        "AMZN": {"base_price": 155.00, "name": "Amazon.com Inc."},
        "NVDA": {"base_price": 875.00, "name": "NVIDIA Corporation"},
        "AMD": {"base_price": 155.00, "name": "Advanced Micro Devices"},
        "NFLX": {"base_price": 485.00, "name": "Netflix Inc."},
    }

    ticker_upper = ticker.upper()
    
    if ticker_upper not in mock_stocks:
        return {
            "status": "error",
            "error_message": f"Stock ticker {ticker} not found in our database",
        }

    try:
        # Generate a realistic price variation (+/- 5% from base)
        base_price = mock_stocks[ticker_upper]["base_price"]
        variation = random.uniform(-0.05, 0.05)  # +/- 5%
        current_price = round(base_price * (1 + variation), 2)
        
        company_name = mock_stocks[ticker_upper]["name"]
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return {
            "status": "success",
            "ticker": ticker_upper,
            "company_name": company_name,
            "price": current_price,
            "timestamp": current_time,
            "note": "This is simulated data for demonstration purposes"
        }

    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error generating stock data: {str(e)}",
        }


# Create the stock analyst agent
stock_analyst = Agent(
    name="stock_analyst",
    model="gemini-2.0-flash",
    description="A stock market assistant that provides mock stock prices for demonstration purposes.",
    instruction="""
    You are a helpful stock market assistant that helps users track stock prices.
    
    IMPORTANT: You work with simulated stock data for demonstration purposes only.
    Always mention that the data is simulated and not real market data.
    
    When asked about stock prices:
    1. Use the get_stock_price tool to fetch simulated prices for requested stocks
    2. Format the response clearly showing the company name, ticker, and current simulated price
    3. Always include a disclaimer that this is demonstration data
    4. If a stock ticker isn't found, suggest some available options
    
    Available stock tickers: AAPL, GOOGL, GOOG, MSFT, TSLA, META, AMZN, NVDA, AMD, NFLX
    
    Example response format:
    "Here are the simulated stock prices:
    - Apple Inc. (AAPL): $175.34 (updated at 2024-04-21 16:30:00)
    - Tesla Inc. (TSLA): $156.78 (updated at 2024-04-21 16:30:00)
    
    Note: This is simulated data for demonstration purposes only, not real market data."
    """,
    tools=[get_stock_price],
)
