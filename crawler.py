# main.py
import yfinance as yf
import pandas as pd
from selector import select_date

print("=== 股票資料爬蟲 ===")
ticker = input("請輸入股票代號或名稱（例如 AAPL, TSLA, 2330.TW）: ")

print("\n請選擇起始日期：")
start_date = select_date("Select Start Date")
print(f"起始日期：{start_date}")

print("\n請選擇結束日期：")
end_date = select_date("Select End Date")
print(f"結束日期：{end_date}")

print("\n下載資料中...")

data = yf.download(ticker, start=start_date, end=end_date)
print(data)
if data.empty:
    print("❌ 找不到該股票或日期區間的資料。")
else:
    output_file = f"{ticker}_{start_date}_{end_date}.xlsx"
    data.to_excel(output_file)
    print(f"✅ 已成功輸出資料：{output_file}")
