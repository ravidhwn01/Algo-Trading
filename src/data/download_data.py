import yfinance as yf
import os
import zipfile

nifty_50_symbols = [
    "RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS",
    "ITC.NS", "LT.NS", "SBIN.NS", "AXISBANK.NS", "BHARTIARTL.NS",
    "HCLTECH.NS", "WIPRO.NS", "MARUTI.NS", "HINDUNILVR.NS", "KOTAKBANK.NS",
    "ULTRACEMCO.NS", "ASIANPAINT.NS", "TITAN.NS", "BAJFINANCE.NS", "ADANIENT.NS",
    "NTPC.NS", "ONGC.NS", "POWERGRID.NS", "BAJAJFINSV.NS", "TATAMOTORS.NS",
    "COALINDIA.NS", "NESTLEIND.NS", "JSWSTEEL.NS", "SUNPHARMA.NS", "TECHM.NS",
    "DIVISLAB.NS", "BPCL.NS", "BRITANNIA.NS", "GRASIM.NS", "CIPLA.NS",
    "HDFCLIFE.NS", "HEROMOTOCO.NS", "DRREDDY.NS", "HINDALCO.NS", "EICHERMOT.NS",
    "BAJAJ-AUTO.NS", "TATACONSUM.NS", "INDUSINDBK.NS", "SBILIFE.NS", "SHREECEM.NS",
    "ADANIPORTS.NS", "APOLLOHOSP.NS", "M&M.NS", "ICICIPRULI.NS", "UPL.NS"
]

intervals = {"1d": "daily", "1wk": "weekly", "1mo": "monthly"}
base_dir = "nifty50_20yr_data"

# Create folders
for label in intervals.values():
    os.makedirs(f"{base_dir}/{label}", exist_ok=True)

# Download data
for symbol in nifty_50_symbols:
    for interval, label in intervals.items():
        print(f"Downloading {symbol} at interval {interval}")
        df = yf.download(symbol, interval=interval, start="2005-01-01", end="2025-07-01")
        if not df.empty:
            path = f"{base_dir}/{label}/{symbol.replace('.NS', '')}_{interval}.csv"
            df.to_csv(path)

# Zip all data
with zipfile.ZipFile("nifty50_20yr_data.zip", 'w') as zipf:
    for label in intervals.values():
        folder = f"{base_dir}/{label}"
        for file in os.listdir(folder):
            zipf.write(os.path.join(folder, file), arcname=f"{label}/{file}")

print("✅ ZIP file created: nifty50_20yr_data.zip")
